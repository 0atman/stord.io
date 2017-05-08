(defproject c "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [metosin/compojure-api "1.1.10"]
                 [com.taoensso/carmine "2.16.0"]
                 [hiccup "1.0.5"]
                 [proto-repl "0.3.1"]]
  :ring {:handler c.core/app :port 5000}
  :uberjar-name "server.jar"
  :profiles {:dev {:plugins [[lein-ring "0.10.0"]]}}
  :min-lein-version "2.0.0")
