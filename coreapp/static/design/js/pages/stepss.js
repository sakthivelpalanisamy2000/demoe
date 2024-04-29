$(".tab-wizard").steps({
  headerTag: "h6",
  bodyTag: "section",
  transitionEffect: "none",
  titleTemplate: '<span class="step">#index#</span> #title#',
  labels: {
    finish: "Submit",
  },
  onFinished: function (event, currentIndex) {
    swal(
      "Your Data  Submitted!",
      "Your Resume will be ready click download button Get your Resume  . Suppose you change the color you can click color palette choose your color and download you resume ."
    );
  },
});

var form = $(".validation-wizard").show();

$(".validation-wizard").steps({
  headerTag: "h6",
  bodyTag: "section",
  transitionEffect: "none",
  titleTemplate: '<span class="step">#index#</span> #title#',
  labels: {
    finish: "Submit",
  },
  onStepChanging: function (event, currentIndex, newIndex) {
    return (
      currentIndex > newIndex ||
      (!(3 === newIndex && Number($("#age-2").val()) < 18) &&
        (currentIndex < newIndex &&
          (form.find(".body:eq(" + newIndex + ") label.error").remove(),
          form.find(".body:eq(" + newIndex + ") .error").removeClass("error")),
        (form.validate().settings.ignore = ":disabled,:hidden"),
        form.valid()))
    );
  },
  onFinishing: function (event, currentIndex) {
    return (form.validate().settings.ignore = ":disabled"), form.valid();
  },
  onFinished: function (event, currentIndex) {
    swal("Your Data  Submitted!", "Details are verified.");
  },
}),
  $(".validation-wizard").validate({
    ignore: "input[type=hidden]",
    errorClass: "text-danger",
    successClass: "text-success",
    highlight: function (element, errorClass) {
      $(element).removeClass(errorClass);
    },
    unhighlight: function (element, errorClass) {
      $(element).removeClass(errorClass);
    },
    errorPlacement: function (error, element) {
      error.insertAfter(element);
    },
    rules: {
      email: {
        email: !0,
      },
    },
  });
