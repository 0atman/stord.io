(ns store.pages
  "Key/Value store"
  (:require [hiccup.page :as page])
  (:use [hiccup.core]))

(defn homepage []
  (page/html5
    [:head
      [:title "title"]
      (page/include-css "https://thebestmotherfucking.website/css/main.css")
      [:meta {:name "viewport" :content "width=device-width, initial-scale=1.0"}]]
    [:body
      [:h1 "A key-value REST collection for simple web apps."]
      [:p
        [:blockquote
          [:span "Think about the ideal way to store data in a web app. Write the code to make it happen."]
          [:author "Aaron Swartz, " [:a {:href "http://webpy.org/philosophy"} "praphrased"]]]]]
    (page/include-js "https://gist.github.com/0atman/a4a620edd9ec1a7c35748f1e5d612e73.js")
    [:p "Play with the api live " [:a {:href "/api-docs/"} "here"] "."]))
