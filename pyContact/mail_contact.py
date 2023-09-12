
contacts = {
    'number': 4,
    'students': 
        [
            {
                'name':'Sarah Holderness',
                'email':'sarah@example.com',
            },
            {
                'name':'John Doe',
                'email':'john@example.com',
            },
            {
                'name':'Ron Snipes',
                'email':'ron@example.com',
            },
            {
                'name':'Wylma Magath',
                'email':'wylma@example.com',
            },
        ],
}

for i in contacts['students']:
    print(i['email'])