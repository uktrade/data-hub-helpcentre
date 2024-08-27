const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "http://localhost:8000/",
    screenshotsFolder: "test-results/screenshots",
    video: true,
    videosFolder: "test-results/videos",
    viewportWidth: 1200,
    viewportHeight: 2000,
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
