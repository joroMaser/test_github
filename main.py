def main():
    print('hello world!')
    from auth import login
    if login:
        print('hi!')
        print('new text')
        
if __name__ == '__main__':
    main()