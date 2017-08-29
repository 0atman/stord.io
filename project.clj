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
                 [ring-basic-authentication "1.0.5"]
                 [org.clojure/data.json "0.2.6"]
                 [com.cemerick/drawbridge "0.0.7"]
                 [ring/ring-jetty-adapter "1.6.1"]
                 [clj-http "3.5.0"]]
  :ring {:handler store.core/app
         :port 5000
         :reload? true}
  :profiles {:dev {:plugins [[lein-ring "0.10.0"]]}}
  :min-lein-version "2.0.0"
  :aot :all)
