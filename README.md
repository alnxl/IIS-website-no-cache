# 使用gulp避免网站缓存
## 第一步将网站发布至指定的路径下
正常发布即可
## 第二步使用python删除js、log、cshtml文件
可参考python文件夹中
## 第三步在gulp.js中创建对对应名称任务并依此在shell执行
注意：如果使用gulp4.0可以将三个任务按顺序执行
1.任务一:gulp-rev生成新名称（使用uglify后出现BUG,暂停使用）
```
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
```
2.任务二:替换json中的名称（如果不是使用的requirejs或者引用是带着.js可跳过此步骤）
```
gulp.src('ESSDWEB2016_dist/js/rev/rev-manifest.json')
        .pipe(replace('.js', ''))
        .pipe(gulp.dest('ESSDWEB2016_dist/js/rev_dist'));
```

3.任务三:替换cshtml中的js名称
```
gulp.src(['ESSDWEB2016_dist/js/rev_dist/rev-manifest.json', 'ESSDWEB2016/Views/**/*.cshtml'])        //- 读取 rev-manifest.json 文件以及需要进行css名替换的文件
    .pipe(revCollector())
    .pipe(bom()) //一定要在输出前引入该包                                               //- 执行文件内css名的替换
    .pipe(gulp.dest('ESSDWEB2016_dist/Views'));  
```
## 注意事项:
1.在任务三中使用.pipe(bom())防止生成新的cshtml中出现中文乱码


