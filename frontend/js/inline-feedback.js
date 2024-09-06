addEventListener("DOMContentLoaded", () => {
  function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(";");
    for (let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == " ") {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }
  token = getCookie("csrftoken");

  class FeedbackForm {
    constructor(baseUrl, token) {
      this.id = null;
      this.baseUrl = baseUrl;
      this.token = token;
      this.isHelpful = null;
      this.headers = {
        "Content-Type": "application/json",
        Accept: "application/json",
        "X-Csrftoken": this.token,
      };
      this.location = new URL(window.location.href);
      this.feedbackFormContainer = document.querySelector(".inline-feedback");
      this.feedbackForm = document.getElementById("feedback-form");
      this.initialFeedbackContainer = document.getElementById(
        "initial-feedback-container"
      );
      this.initialFeedbackButtons = this.initialFeedbackContainer.querySelectorAll(
        "button"
      );
      this.postInitialFeedbackContainer = document.getElementById(
        "post-initial-feedback-container"
      );
      this.positiveFeedbackForm = document.getElementById("positive-feedback");
      this.negativeFeedbackForm = document.getElementById("negative-feedback");

      this.feedbackFormContainer.classList.remove("feedback-complete");
      this.positiveFeedbackForm.style.display = "none";
      this.negativeFeedbackForm.style.display = "none";
      this.postInitialFeedbackContainer.style.display = "none";
      this.loadingEl = document.querySelector(".loading");
      this.loadingEl.style.display = "none";
    }

    loading(loading) {
      this.loadingEl.style.display = loading ? "block" : "none";
    }

    handleError(response) {
      this.initialFeedbackContainer.innerHTML = `<p class="govuk-body inline-feedback__error">${response.message}: ${response.error}</p>`;
    }

    async handleFetch(endpoint, requestOptions, isComplete = false) {
      let data = {};
      let status = 500;
      try {
        this.loading(true);
        const response = await fetch(
          `${this.baseUrl}${endpoint}`,
          requestOptions
        );
        data = await response.json();
        this.id = data.id;
        this.isHelpful = data.was_this_page_helpful;
        this.loading(false);
        status = response.status;
        if (status === 403) {
          throw "403 forbidden";
        }
        if (isComplete) {
          this.closeForm();
        } else {
          this.showPostInitialFeedbackForm(this.id, this.isHelpful);
        }
      } catch (error) {
        data = { message: "Error", error: error };
        status = 500;
      }
      return { data, status };
    }

    async postInitialFeedback(initial) {
      const response = await this.handleFetch("/api/v1/inline_feedback", {
        method: "POST",
        body: JSON.stringify({
          was_this_page_helpful: initial,
          location: this.location.pathname,
        }),
        headers: {
          ...this.headers,
        },
      });
      if (response.data.error) {
        this.handleError(response.data);
        return;
      }
    }

    async updateInitialFeedback(payload) {
      const response = await this.handleFetch(
        `/api/v1/inline_feedback/${this.id}`,
        {
          method: "PATCH",
          body: JSON.stringify({
            inline_feedback_choices: payload.choices,
            more_detail: payload.moreDetail,
          }),
          headers: {
            ...this.headers,
          },
        },
        true
      );
      if (response.data.error) {
        this.handleError(response.data);
        return;
      }
      this.feedbackFormContainer.classList.add("feedback-complete");
    }

    showPostInitialFeedbackForm(id, isHelpful) {
      this.initialFeedbackContainer.style.display = "none";
      this.postInitialFeedbackContainer.style.display = "block";
      this.feedbackForm.style.display = "block";
      isHelpful
        ? (this.positiveFeedbackForm.style.display = "block")
        : (this.negativeFeedbackForm.style.display = "block");

      this.feedbackForm.onsubmit = (event) => {
        event.preventDefault();
        const Form = new FormData(this.feedbackForm);
        const choices = Form.getAll("choices").join(",");
        const moreDetail = isHelpful
          ? Form.getAll("more-detail")[0]
          : Form.getAll("more-detail")[1];
        const payload = {
          choices,
          moreDetail,
        };
        this.updateInitialFeedback(payload);
      };
    }

    resetForm() {
      this.id = null;
      this.isHelpful = null;
      this.feedbackForm.style.display = "none";
      this.initialFeedbackContainer.style.display = "inline-flex";
      this.postInitialFeedbackContainer.style.display = "none";
      this.positiveFeedbackForm.style.display = "none";
      this.negativeFeedbackForm.style.display = "none";
    }

    closeForm() {
      this.feedbackForm.style.display = "none";
      this.postInitialFeedbackContainer.style.display = "block";
    }

    init() {
      Array.from(this.initialFeedbackButtons).map((button) => {
        button.addEventListener("click", (event) => {
          event.preventDefault();
          InlineFeedbackForm.postInitialFeedback(event.target.value);
        });
      });

      document
        .getElementById("cancel-link")
        .addEventListener("click", (event) => {
          event.preventDefault();
          this.resetForm();
        });
    }
  }

  const InlineFeedbackForm = new FeedbackForm(
    new URL(window.location.origin),
    token
  );
  InlineFeedbackForm.init();
});
