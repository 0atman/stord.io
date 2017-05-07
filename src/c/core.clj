(ns c.core
  "test"
  (:require [taoensso.carmine :as redis]
            [schema.core :as s]
            [compojure.api.sweet :refer (api context GET POST defapi)]
            [ring.util.http-response :refer (ok)])
  (:gen-class))


(defmacro transaction [& body]
  "Start redis transaction"
  `(redis/wcar
    {:spec {:host "localhost" :port 6379}}
    ~@body))

(def app
 (api
   {:swagger
    {:ui "/api-docs"
     :spec "/swagger.json"
     :data {:info {:title "Stord API"
                   :description "Stord Api example"}
            :tags [{:name "api", :description "some apis"}]}}}

   (context "/api" []
     :tags ["api"]

     (GET "/key" []
        :summary "pulls the key `name` from redis"
        :query-params [name :- String]
        :return {:message String}
        (ok {:message (transaction (redis/get name))}))

     (POST "/key" [data]
        :summary "Updates key `name` to `data`"
        :query-params [name :- String]
        :return {:message String}
        (ok {:message (transaction (redis/set name data))})))))
