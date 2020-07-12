def show_client_info(**info):
    print('客户姓名', info['name'])
    print('年龄', info['age'])
    print('客户性别', info['gender'])





if __name__ == '__main__':
    show_client_info(name='Bob', age=27, gender='男')