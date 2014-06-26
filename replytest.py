import web
import xmltodict
import xml.etree.cElementTree as ET

urls = (
        '/', 'index',
        '/12306','wechat'
       )

class index:
    def GET(self):
        return "hello"

class wechat:
    def POST(self):
        print web.data()
        user_input = xmltodict.parse(web.data())
        to_user_name = user_input['xml']['ToUserName']
        from_user_name = user_input['xml']['FromUserName']
        create_time = user_input['xml']['CreateTime']
        msg_type = user_input['xml']['MsgType']
        content = user_input['xml']['Content']
        msg_id = user_input['xml']['MsgId']
        
        root = ET.Element('xml')
        ToUserName = ET.Element('ToUserName')
        FromUserName = ET.Element('FromUserName')
        CreateTime = ET.Element('CreateTime')
        MsgType = ET.Element('MsgType')
        Content = ET.Element('Content')
        MsgId = ET.Element('MsgId')
        root.extend((ToUserName,FromUserName,CreateTime,MsgType,Content))
        tree = ET.ElementTree(root)

        ToUserName.text = from_user_name
        FromUserName.text = to_user_name
        CreateTime.text = create_time
        MsgType.text = msg_type
        Content.text = content + " With Alex"
        MsgId.text = msg_id
        tree = ET.ElementTree(root)
        return ET.tostring(root,encoding='utf8', method='xml')

if __name__ == "__main__":
    app = web.application (urls, globals())
    app.run()
