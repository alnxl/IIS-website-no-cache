#
# WEB-Gulp
#
python F:\PythonProject\IIS-website-no-cache\python\run.py --source_file_path=E:\IIS_Data\ESSDWEB2016 --empty_file_path=E:\\IIS_Data\ESSDWEB2016_dist
cd E:\IIS_Data
gulp minJsAndCreateJson
gulp replaceURL
gulp ESSDWEB2016
pause