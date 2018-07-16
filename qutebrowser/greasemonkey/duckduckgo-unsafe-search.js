// ==UserScript==
// @name        DuckDuckGo unsafe search
// @description Always disables safe search on DuckDuckGo
// @namespace   karasiq
// @include     https://duckduckgo.com/*
// @version     1
// @grant       none
// ==/UserScript==

function duckduckgoDisableSafeSearch() {
  var button = document.querySelector("div.dropdown--safe-search a");
  if (button && button.text.contains("Strict")) {
    button.click();
    var offButton = document.querySelector("div.modal--dropdown--safe-search a[data-value='-2']");
    if (offButton) offButton.click();
  }
}

if (document && document.addEventListener) {
  document.addEventListener("DOMContentLoaded", duckduckgoDisableSafeSearch, false);
}