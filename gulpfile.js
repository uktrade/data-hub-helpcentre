'use strict';
const path = require('path');
const gulp = require('gulp');
const sass = require('gulp-sass');
const sourcemaps = require('gulp-sourcemaps');
const del = require('del');

const PROJECT_DIR = path.resolve(__dirname);
const SASS_FILES = `${PROJECT_DIR}/frontend/sass/**/*.scss`;
const STATIC_DIR = `${PROJECT_DIR}/helpdesk/helpdesk/static`;
const CSS_DIR = `${STATIC_DIR}/css`;
const CSS_FILES = `${CSS_DIR}/**/*.css`;
const CSS_MAPS = `${CSS_DIR}/**/*.css.map`;
const GOVUK_PATH = `${PROJECT_DIR}/node_modules/govuk-frontend`;
const GOVUK_ASSETS_PATH = `${GOVUK_PATH}/assets`;
const ASSETS_DEST = `${STATIC_DIR}/assets`;
const JS_DEST = `${STATIC_DIR}/js`;

gulp.task('clean', function() {
  return del([CSS_FILES, CSS_MAPS]);
});

gulp.task('copy-govuk-assets', function() {
  return gulp
    .src([`${GOVUK_ASSETS_PATH}/**/*`], { base: GOVUK_ASSETS_PATH })
    .pipe(gulp.dest(ASSETS_DEST));
});

gulp.task('copy-govuk-js', function() {
  return gulp.src([`${GOVUK_PATH}/all.js`]).pipe(gulp.dest(JS_DEST));
});

gulp.task('sass:compile', function() {
  return gulp
    .src(SASS_FILES)
    .pipe(sourcemaps.init())
    .pipe(
      sass({
        includePaths: ['./conf/'],
        outputStyle: 'compressed'
      }).on('error', sass.logError)
    )
    .pipe(sourcemaps.write('./maps'))
    .pipe(gulp.dest(CSS_DIR));
});

gulp.task('sass:watch', function() {
  gulp.watch([SASS_FILES], gulp.series('sass:compile'));
});

gulp.task('sass', gulp.series('clean', 'sass:compile'));

gulp.task(
  'default',
  gulp.series(['sass', 'copy-govuk-assets', 'copy-govuk-js'])
);
