function test_inject() {
  window.alert("Hello, world!")
}

str = parent.document.getElementById("results_results").innerHTML
if (str && str.length > 0) {
  test_inject()
}
