// gulp
var gulp = require('gulp');

// plugins
var connect = require('gulp-connect');
var jshint = require('gulp-jshint');
var uglify = require('gulp-uglify');
var minifyCSS = require('gulp-minify-css');
var clean = require('gulp-clean');
var browserify = require('browserify');
var sass = require('gulp-sass');
var gutil = require('gulp-util');
var watchify = require('watchify');
var stream = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');
var sourcemaps = require('gulp-sourcemaps');
var gulpNgConfig = require('gulp-ng-config')
var rename = require('gulp-rename');

var argv = require('yargs').argv;

var bases = 
{
    app: 'app/',
    build: 'build/',
};

var paths = 
{
    initjs: ['./app/init.js'],
    sass: ['app/app.scss'],
    static: ['app/**/*.html', 'app/**/img/**', 'app/**/images/**', 'app/**/fonts/**'],
    config: ['app/config/config.js']
};

function build_scripts()
{
    var b = browserify(paths.initjs);

    return b.bundle()
        .on('error', gutil.log)
        .pipe(stream('app.min.js'))
        .pipe(buffer())
        .pipe(uglify())
        .pipe(gulp.dest('./build'));
}

function build_styles()
{
    console.log("build_styles");

    gulp.src(paths.sass)
        .pipe(sass())
        .on('error', gutil.log)
        .pipe(minifyCSS())
        .on('error', gutil.log)
        .pipe(gulp.dest(bases.build));
}

function copy_static()
{
    gulp.src(paths.static)
        .pipe(gulp.dest(bases.build));
}

function watch_styles()
{
    build_styles();
    gulp.watch(bases.app + '**/*.scss', build_styles);
}

function watch_static()
{
    var copier = function () 
    {
        console.log("copy_static");

        gulp.src([bases.build+'**/*.html', bases.build+'**/img', bases.build+'**/images', bases.build+'**/images'], {read: false})
            .pipe(clean());

        copy_static();
    }

    copier();

    gulp.watch(paths.static, copier);
}

function watch_config()
{
    build_config();
    gulp.watch(paths.config, build_config);
}

function watch_scripts()
{
    var browserify_opt = 
    {
        cache: {},
        packageCache: {}, 
        fullPaths: true,
        insertGlobals: true,
        debug: true
    };

    var b = watchify(browserify(paths.initjs, browserify_opt));

    var builder = function() 
    {
        console.log("build_scripts");

        return b.bundle()
            .on('error', gutil.log)
            .pipe(stream('app.min.js'))
            .pipe(buffer())
            .pipe(sourcemaps.init({loadMaps: true}))
            .pipe(sourcemaps.write('./'))
            .pipe(gulp.dest('./build'));
    }

    b.on('update', builder);

    return builder();
}

function run_server(port)
{
    connect.server
    (
        {
            root: bases.build,
            port: port
        }
    );
}

function build_config()
{
    var env = argv.env == undefined ? 'local' : argv.env;
    return gulp.src(paths.config)
        .pipe(gulpNgConfig('AppModule', {environment: env, createModule: false}))
        .pipe(rename('config.js'))
        .pipe(gulp.dest('./app'));
}

gulp.task
(
    'verify', 
    function() 
    {
        gulp.src('./app/**/*.js')
            .pipe(jshint())
            .pipe(jshint.reporter());
    }
);

gulp.task
(
    'clean', 
    function() 
    {
        return gulp.src(bases.build)
                   .pipe(clean());
    }
);

gulp.task
(
    'server',
    ['clean'],
    function() 
    {
        watch_config();
        watch_styles();
        watch_static();
        watch_scripts();
        run_server(8000);
    }
);

function build()
{
    build_config();
    build_styles();
    copy_static();
    build_scripts();
}

gulp.task
(
    'build',
    ['clean'],
    build
);

gulp.task
(
    'default',
    ['clean'],
    function() 
    {
        build();
        run_server(8000);
    }
);
