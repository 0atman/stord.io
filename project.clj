(defproject store "0.2.0"
  :description "FIXME: write description"
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [metosin/compojure-api "1.1.10"]
                 [com.taoensso/carmine "2.16.0"]
                 [hiccup "1.0.5"]
                 [proto-repl "0.3.1"]
                 [org.clojure/tools.nrepl "0.2.12"]
                 [ring "1.6.1"]
                 [lein-ring "0.10.0"]
                 [ring/ring-jetty-adapter "1.6.1"]]
  :ring {:handler store.core/app
         :port 5000
         :nrepl {:start? true
                 :port 9998}}
  :profiles {:dev {:plugins [[lein-ring "0.10.0"]]}}
  :min-lein-version "2.0.0")
