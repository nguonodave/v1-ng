// // HAMBURGER AND SIDE-MENU ---------------------------------------------------------------------------------------------------------------
const hamburger = document.getElementById("hamburger");
const side_menu = document.getElementById("side-menu");
const html = document.querySelector("html");
const main = document.querySelector("main");
const footer = document.querySelector("footer");

hamburger.onclick = function () {
  hamburger.classList.toggle("active");
  side_menu.classList.toggle("active");
  html.classList.toggle("overflow-y-hidden");
  main.classList.toggle("blur-active");
  footer.classList.toggle("blur-active");
};

document.onclick = function (clickEvent) {
  if (
    clickEvent.target.id !== "side-menu" &&
    clickEvent.target.id !== "hamburger" &&
    clickEvent.target.id !== "side-inner-menu" &&
    clickEvent.target.id !== "side-nav-content"
  ) {
    hamburger.classList.remove("active");
    side_menu.classList.remove("active");
    html.classList.remove("overflow-y-hidden");
    main.classList.remove("blur-active");
    footer.classList.remove("blur-active");
  }
};

// // DARK LIGHT THEME TOGGLE ---------------------------------------------------------------------------------------------------------------
const theme_icon = document.getElementById("theme-icon");
const savedTheme = localStorage.getItem("theme");

if (savedTheme === "light-mode-settings") {
  document.body.classList.add(savedTheme);
  theme_icon.className = "bx bx-moon";
} else {
  document.body.classList.add("dark-mode-settings");
  theme_icon.className = "bx bx-sun";
}

theme_icon.onclick = function () {
  document.body.classList.toggle("light-mode-settings");
  if (document.body.classList.contains("light-mode-settings")) {
    theme_icon.className = "bx bx-moon";
    localStorage.setItem("theme", "light-mode-settings");
  } else {
    theme_icon.className = "bx bx-sun";
    localStorage.setItem("theme", "dark-mode-settings");
  }
};

// // TABBED COMPONENTS ---------------------------------------------------------------------------------------------------------------
// Responsive Nav --------------------------------------
const btn_left = document.querySelector(".left-btn");
const btn_right = document.querySelector(".right-btn");
const tab_menu = document.querySelector(".tab-menu");

const IconVisibility = () => {
  let scrollLeftValue = Math.ceil(tab_menu.scrollLeft);
  let scrollableWidth = tab_menu.scrollWidth - tab_menu.clientWidth;

  btn_left.style.display = scrollLeftValue > 0 ? "flex" : "none";
  btn_right.style.display = scrollableWidth > scrollLeftValue ? "flex" : "none";
};

btn_right.addEventListener("click", () => {
  tab_menu.scrollLeft += 150;
  setTimeout(() => IconVisibility(), 50);
});

btn_left.addEventListener("click", () => {
  tab_menu.scrollLeft -= 150;
  setTimeout(() => IconVisibility(), 50);
});

window.onload = function () {
  btn_right.style.display =
    tab_menu.scrollWidth > tab_menu.clientWidth ||
    tab_menu.scrollWidth >= window.innerWidth
      ? "flex"
      : "none";
  btn_left.style.display =
    tab_menu.scrollWidth >= window.innerWidth ? "" : "none";
};

window.onresize = function () {
  btn_right.style.display =
    tab_menu.scrollWidth > tab_menu.clientWidth ||
    tab_menu.scrollWidth >= window.innerWidth
      ? "flex"
      : "none";
  btn_left.style.display =
    tab_menu.scrollWidth >= window.innerWidth ? "" : "none";

  let scrollLeftValue = Math.round(tab_menu.scrollLeft);

  btn_left.style.display = scrollLeftValue > 0 ? "flex" : "none";
};

// Responsive Nav --------------------------------------
let activeDrag = false;

tab_menu.addEventListener("mousemove", (drag) => {
  if (!activeDrag) return;
  tab_menu.scrollLeft -= drag.movementX;
  IconVisibility();
  tab_menu.classList.add("dragging");
});

document.addEventListener("mouseup", () => {
  activeDrag = false;
  tab_menu.classList.remove("dragging");
});

tab_menu.addEventListener("mousedown", () => {
  activeDrag = true;
});

// Show content on tab click -----------------------------
const tabs = document.querySelectorAll(".tab");
const tab_btns = document.querySelectorAll(".tab-btn");

const tab_nav = function (tabBtnClick) {
  tab_btns.forEach((tab_btn) => {
    tab_btn.classList.remove("active");
  });

  tabs.forEach((tab) => {
    tab.classList.remove("active");
  });

  tab_btns[tabBtnClick].classList.add("active");
  tabs[tabBtnClick].classList.add("active");
};

tab_btns.forEach((tab_btn, i) => {
  tab_btn.addEventListener("click", () => {
    tab_nav(i);
  });
});

// // // COPYRIGHT DYNAMIC DATE------------------------------------------------------------------------------------------------------
// const date = new Date();
// document.querySelector(".year").innerHTML = date.getFullYear();

// // CONTACT FORM VALIDATION------------------------------------------------------------------------------------------------------
function validateForm() {
  let name = document.forms["contactForm"]["name"].value;
  let email = document.forms["contactForm"]["email"].value;
  let phone = document.forms["contactForm"]["phone"].value;
  let message = document.forms["contactForm"]["message"].value;

  if (name == "" || hasNumber(name)) {
    alert("Name must be filled out and must only contain letters");
    return false;
  } else if (email == "" && phone == "") {
    alert("Email or phone must be filled out");
    return false;
  } else if (!email.includes("@")) {
    alert("Email does not seem to be valid");
    return false;
  } else if (isNaN(phone)) {
    alert("Phone number seems to contain letters");
    return false;
  } else if (message == "") {
    alert("Message must be filled out");
    return false;
  } else {
    // confirm or cancel
    var bodyMessage =
      "Name: " +
      name +
      "<br/> Email: " +
      email +
      "<br/> Phone: " +
      phone +
      "<br/><br/>" +
      message;

    Email.send({
      SecureToken: "f754b95e-c2be-4cd6-9c4d-1170b0a20149",
      To: "nguonodave.portfolio@gmail.com",
      From: "nguonodave.portfolio@gmail.com",
      Subject: "NEW PORTFOLIO CONTACT FROM",
      Body: bodyMessage,
    });
    return confirm("This message will be sent to David. You sure?");
  }
}

function hasNumber(myString) {
  return /\d/.test(myString);
}

// // // CONTACT FORM EMAIL SUBMISSION------------------------------------------------------------------------------------------------------
// var submit = document.getElementById("submit");

// submit.addEventListener("click", function (e) {
//   e.preventDefault();
//   var name = document.getElementById("name").value;
//   var email = document.getElementById("email").value;
//   var phone = document.getElementById("phone").value;
//   var message = document.getElementById("message").value;
//   bodyMessage =
//     "Name: " +
//     name +
//     "<br/> Email: " +
//     email +
//     "<br/> Phone: " +
//     phone +
//     "<br/>" +
//     message;

//   Email.send({
//     SecureToken: "f754b95e-c2be-4cd6-9c4d-1170b0a20149",
//     To: "nguonodave.portfolio@gmail.com",
//     From: "nguonodave.portfolio@gmail.com",
//     Subject: "NEW PORTFOLIO CONTACT FROM",
//     Body: bodyMessage,
//   }).then((message) => alert(message));
// });
