var gulp = require('gulp');
var bom = require('gulp-bom');
var jshint = require("gulp-jshint"); 
var uglify = require('gulp-uglify');
var rev = require('gulp-rev');
var revCollector = require('gulp-rev-collector');	
var cssmin = require('gulp-clean-css');
var imagemin = require('gulp-imagemin');
var zip = require('gulp-zip');
var replace = require('gulp-replace'); 
var rename = require('gulp-rename');
gulp.task('default', function() {
  console.log("hello world")
});
gulp.task('minJsAndCreateJson', function() {
    console.log("压缩业务逻辑js代码,执行创建命名json")
	//压缩业务逻辑js代码
    gulp.src('ESSDWEB2016/js/**/*.js',{base:'.'})
    	// .pipe(jshint())
    	// .pipe(uglify({ mangle: { toplevel: true } }))
    	.pipe(rev({merge:true}))
    	.pipe(rename(function (path) {
           path.dirname = path.dirname.replace('ESSDWEB2016', '') 
        }))
    	.pipe(gulp.dest('ESSDWEB2016_dist'))
    	.pipe(rev.manifest())
        .pipe(gulp.dest('ESSDWEB2016_dist/js/rev/'));
});
gulp.task('replaceURL',function(){
    console.log("替换js文件名称中的名称")
    gulp.src('ESSDWEB2016_dist/js/rev/rev-manifest.json')
        .pipe(replace('.js', ''))
        .pipe(gulp.dest('ESSDWEB2016_dist/js/rev_dist'));

});
gulp.task('ESSDWEB2016', function() {
    console.log("替换html中的js名称")
    gulp.src(['ESSDWEB2016_dist/js/rev_dist/rev-manifest.json', 'ESSDWEB2016/Views/**/*.cshtml'])        
    .pipe(revCollector())
    .pipe(bom()) //一定要在输出前引入该包                                     
    .pipe(gulp.dest('ESSDWEB2016_dist/Views'));     
});

