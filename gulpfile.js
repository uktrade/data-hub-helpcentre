"use strict";
import path from "path";
import { fileURLToPath } from "url";
import gulp from "gulp";
import gulpSass from "gulp-sass";
import { deleteAsync } from "del";
import dartSass from "sass";
const sass = gulpSass(dartSass)

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PROJECT_DIR = path.resolve(__dirname);
const SASS_FILES = `${PROJECT_DIR}/frontend/sass/**/*.scss`;
const JS_FILES = `${PROJECT_DIR}/frontend/js/**/*.js`;
const STATIC_DIR = `${PROJECT_DIR}/static`;
const CSS_DIR = `${STATIC_DIR}/css`;
const CSS_FILES = `${CSS_DIR}/**/*.css`;
const CSS_MAPS = `${CSS_DIR}/**/*.css.map`;
const GOVUK_PATH = `${PROJECT_DIR}/node_modules/govuk-frontend/govuk`;
const GOVUK_ASSETS_PATH = `${GOVUK_PATH}/assets`;
const ASSETS_DEST = `${STATIC_DIR}/assets`;
const JS_DEST = `${STATIC_DIR}/js`;

const sassOptions = {
  // includePaths: ['./conf/'],
  outputStyle: "compressed",
};

gulp.task("clean", function () {
  const fonts = `${ASSETS_DEST}/fonts`;
  return deleteAsync([CSS_FILES, CSS_MAPS, fonts]);
});

gulp.task("copy-govuk-assets", function () {
  return gulp
    .src([`${GOVUK_ASSETS_PATH}/**/*`], { base: GOVUK_ASSETS_PATH })
    .pipe(gulp.dest(ASSETS_DEST));
});

gulp.task("copy-govuk-js", function () {
  return gulp
    .src([JS_FILES, `${GOVUK_PATH}/all.js`])
    .pipe(gulp.dest(JS_DEST));
});

gulp.task("sass:compile", function () {
  return gulp
    .src(SASS_FILES)
    .pipe(sass(sassOptions))
    .pipe(gulp.dest(CSS_DIR));
});

gulp.task("sass:watch", function () {
  gulp.watch([SASS_FILES], gulp.series("sass:compile"));
});

gulp.task("sass", gulp.series("clean", "sass:compile"));

gulp.task(
  "default",
  gulp.series(["sass", "copy-govuk-assets", "copy-govuk-js"])
);
