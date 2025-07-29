$(document).ready(() => {

  $("#pageName").text(""); 
  const title = "BlogSpace";
  let i = 0;

  function type() {
    if (i < title.length) {
      $("#pageName").append(title.charAt(i));
      i++;
      setTimeout(type, 150);
    } else {$(pageName).removeClass("typing");}
  }

  type();

  $(".addPostBtn").click(() => {
    $("#newPost").toggleClass("hidden");
  });

  $(document).click((event) => {
    if (!$(event.target).closest("#newPost, .addPostBtn").length) {
      $("#newPost").addClass("hidden");
    }
  });

  const updateCounter = (inputSelector, counterSelector, max) => {
    $(inputSelector).on("input", function () {
      const count = $(this).val().length;
      if (count === max) {
        $(counterSelector).css("color", "red")
      } else {
        $(counterSelector).css("color", "grey")
      }
      $(counterSelector).text(`${count}/${max}`);
    });

    const initialCount = $(inputSelector).val().length;
    $(counterSelector).text(`${initialCount}/${max}`);
  };

  updateCounter('#postName', '#title-counter', 30);
  updateCounter('#postContent', '#content-counter', 500);
});
