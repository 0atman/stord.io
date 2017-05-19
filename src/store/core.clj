(ns store.core
  "Key/Value store"
  (:require [taoensso.carmine :as redis]
            [schema.core :as s]
            [compojure.api.sweet :refer (api context GET POST defapi)]
            [ring.util.http-response :refer (ok not-found unauthorized!)]
            [compojure.api.exception :as ex]
            [ring.util.http-response :as response]
            [clojure.data.json :as json]
            [store.pages :as pages])
  (:gen-class))

(defmacro transaction
  "Start redis transaction"
  [& body]
  `(redis/wcar
    {:spec {:uri (get (System/getenv) "REDIS_URL" "redis://localhost:6379")}}
    ~@body))

(defn hget
  "Get the value of a hash field."
  [key field]
  (transaction (redis/hget key field)))

(defn hset
  "Set the string value of a hash field."
  [key field value]
  (transaction (redis/hset key field value)))

(defn check_auth
  "Returns true if the auth key exists."
  [auth]
  (boolean (hget "auth" auth)))

(defn uuid
  "return a random uuid string."
  []
  (str (java.util.UUID/randomUUID)))

(def app
  (api
    {:swagger
      {:ui "/api-docs"
       :spec "/swagger.json"
       :data {:info {:title "Stord API"}
                    :description "Stord Api"}
             :tags [{:name "api", :description "apis"}]}}

   (GET "/" [] :summary "Homepage" (pages/homepage))

;   (context "/auth" []
;     :summary "Auth stuff"
;     :tags ["auth"]
;
;     (GET "/register/:email" []
;       :summary "adds a new api key registered to `email`"
;       :path-params [email :- String]
;       :return {:created String}
;       (let [new_auth (uuid)]
;         (hset "auth" new_auth email)
;         (ok {:created new_auth}))))


   (context "/api/:auth" []
     :summary "K/V API"
     :tags ["api"]
     :path-params [auth :- String]

     (GET "/:name" []
        :summary "pulls the key `name` from the db"
        :path-params [name :- String]
        :return {:message String}
        (if (check_auth auth)
          (let [value (hget auth name)]
            (if (string? value)
              (ok {:message value})
              (not-found {:message (str "Key not found: " name)})))
          (unauthorized! "Invalid auth key")))


     (GET "/:name/json" []
        :summary "pulls the key `name` from the db and attempts to decode the stored json body"
        :path-params [name :- String]
        (if (check_auth auth)
          (let [value (hget auth name)]
            (if (string? value)
              (ok (json/read-str value))
              (not-found {:message (str "Key not found: " name)})))
          (unauthorized! "Invalid auth key")))


     (POST "/:name" [data]
        :summary "Updates key `name` to `data`"
        :path-params [name :- String]
        :return {:message String}
        (if (check_auth auth)
          (let [redis_code (hset auth name data)]
            (if (= 0 redis_code)
              (ok {:message "OK. Key updated."})
              (ok {:message "OK. Key created."})))
          (unauthorized! "Invalid auth key."))))))
