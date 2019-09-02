
http://172.22.118.25/ctas/ajaxpro/CExam.CPractice,App_Web_tzfdzrj8.ashx
GetJSONChapterList
{}
返回：章节ID


http://172.22.118.25/ctas/ajaxpro/CExam.CPractice,App_Web_tzfdzrj8.ashx
GetJSONProgramList
{"cChapterID":"241"}
{"cChapterID":"【章节ID】"}
返回：程序ID


http://172.22.118.25/ctas/ajaxpro/CExam.CPractice,App_Web_tzfdzrj8.ashx
GetJSONTest
{"strTestParam":"<cTest><cProgram>ch01_01</cProgram><cQuestionIndex>0</cQuestionIndex></cTest>"}
{"strTestParam":"<cTest><cProgram>【程序ID】</cProgram><cQuestionIndex>【第几题】</cQuestionIndex></cTest>"}
返回：程序、题目、选项
注：有题号


http://172.22.118.25/ctas/ajaxpro/CExam.CPractice,App_Web_tzfdzrj8.ashx
GetJSONSummary
{"strTestParam":"<cTestParam><cQuestion>21169</cQuestion><cUserAnswer>D</cUserAnswer></cTestParam>"}
{"strTestParam":"<cTestParam><cQuestion>【题号】</cQuestion><cUserAnswer>【选项】</cUserAnswer></cTestParam>"}
返回：错误解析


http://172.22.118.25/ctas/ajaxpro/CExam.CPractice,App_Web_tzfdzrj8.ashx
WriteLog
{"strTestParam":"<cTestParam><cQuestion>21169</cQuestion><cUserAnswer>D</cUserAnswer></cTestParam>"}
{"strTestParam":"<cTestParam><cQuestion>【题号】</cQuestion><cUserAnswer>【选项】</cUserAnswer></cTestParam>"}


http://172.22.118.25/ctas/ajaxpro/CExam.CPractice,App_Web_tzfdzrj8.ashx
IsOrNotTrue
{"strTestParam":"<cTestParam><cQuestion>21165</cQuestion><cUserAnswer>A</cUserAnswer></cTestParam>"}
{"strTestParam":"<cTestParam><cQuestion>【题号】</cQuestion><cUserAnswer>【选项】</cUserAnswer></cTestParam>"}
返回：
正确 = 1;/*
错误 = 0;/*



http://172.22.118.25/ctas/ajaxpro/CExam.CUserExamList,App_Web_c318vtbf.ashx
GetJSONCTRList
{}
返回：考试列表


http://172.22.118.25/ctas/ajaxpro/CExam.StudReportManage,App_Web_c318vtbf.ashx
GetJSONCTRList
{}
返回：练习统计


http://172.22.118.25/ctas/ajaxpro/CExam.StuIndex,App_Web_c318vtbf.ashx
GetJSONUser
{}
返回：姓名、班级


http://172.22.118.25/ctas/ajaxpro/CExam.CUserManage,App_Web_tzfdzrj8.ashx
SetNewUserPassword
{"strOldPwd":"123456","strNewPwd":"123456789"}
{"strOldPwd":"【旧密码】","strNewPwd":"【新密码】"}
返回：   查找：false 修改失败
        查找：true 修改成功




http://172.22.118.25/ctas/ajaxpro/CExam.Login,App_Web_c318vtbf.ashx
UserLogin
{"strUserId":"2016214224123123","strPwd":"1234564646"}
{"strUserId":"【ID】","strPwd":"【密码】"}
返回：

账号或密码错误
    null; r.error = {"Message":"No matched record","Type":"System.Exception"};/*

登录成功,查找该字符串即可
    true


