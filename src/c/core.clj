(ns c.core
  "test"
  (:require [taoensso.carmine :as redis]
            [schema.core :as s]
            [compojure.api.sweet :refer (api context GET POST defapi)]
            [ring.util.http-response :refer (ok not-found unauthorized!)]
            [compojure.api.exception :as ex]
            [ring.util.http-response :as response])
  (:gen-class))

(defmacro transaction [& body]
  "Start redis transaction"
  `(redis/wcar
    {:spec {:url (get (System/getenv) "REDIS_URL" "redis://localhost:6379")}}
    ~@body))

(defn check_auth [auth]
  "Returns true if the auth key exists"
  (str (transaction (redis/hget "auth" auth))))

(defn uuid [] (str (java.util.UUID/randomUUID)))

(defn custom-handler [f type]
  (fn [^Exception e data request]
    (f {:message (.getMessage e), :type type})))

(def app
  (api
    {:swagger
      {:ui "/api-docs"
       :spec "/swagger.json"
       :data {:info {:title "Stord API"}
                    :description "Stord Api example"}
             :tags [{:name "api", :description "some apis"}]}}


   (GET "/register/:email" []
     :summary "adds a new uuid key to the auth hash, with `email` key"
     :path-params [email :- String]
     :return {:created String}
     (let [new_auth (uuid)]
       (transaction (redis/hset "auth" new_auth email))
       (ok {:created new_auth})))


   (context "/api/:auth" []
     :tags ["api"]
     :path-params [auth :- String]

     (GET "/:name" []
        :summary "pulls the key `name` from redis"
        :path-params [name :- String]
        :return {:message String}
        (if (check_auth auth)
          (let [value (transaction (redis/hget auth name))]
            (if (string? value)
              (ok {:message value})
              (not-found {:message (str "Not found: " name)})))
          (unauthorized! "Invalid auth key")))

     (POST "/:name" [data]
        :summary "Updates key `name` to `data`"
        :path-params [name :- String]
        :return {:message String}
        (if (check_auth auth)
          (let [redis_code (transaction (redis/hset auth name data))]
            (if (= 0 redis_code)
              (ok {:message "OK"})))
          (unauthorized! "Invalid auth key for post"))))))
