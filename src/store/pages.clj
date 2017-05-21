(ns store.pages
  "Key/Value store"
  (:require [hiccup.page :as page])
  (:use [hiccup.core]))

(defn homepage []
  (page/html5
    [:head
      [:title "Store: A lightweight key-value REST collection for simple web apps."]
      (page/include-css "https://thebestmotherfucking.website/css/main.css")
      [:meta {:name "viewport" :content "width=device-width, initial-scale=1.0"}]]
    [:body
      [:h1 "A key-value REST collection for simple web apps."]
      [:p
        [:blockquote
          [:span "Think about the ideal way to store data in a web app. Write the code to make it happen."]
          [:author "Aaron Swartz, " [:a {:href "http://webpy.org/philosophy"} "praphrased"]]]]]
    (page/include-js "https://gist.github.com/0atman/a4a620edd9ec1a7c35748f1e5d612e73.js")
    [:p "Play with the public api live "
        [:a {:href "/api-docs/"} "here"] ". "
        "Use the sandbox api key " [:code "[sandbox]"] " to test with. "
        "Sandbox data is free forever. Use it for IOT apps, prototypes or anything else you can think of!"]
    [:p "To secure your own data, please buy an API Key. "
        "Prices start at $1 for 1,000 keys and the proceeds help support "
        [:a {:href "http://0atman.com"} "me "] " make more awesome services like this one. Thanks!"]

    (page/include-js "https://gumroad.com/js/gumroad.js")
    [:a.gumroad-button {:href "https://gum.co/l/EviMe" :target "_blank"} "Buy an API Key"]))
