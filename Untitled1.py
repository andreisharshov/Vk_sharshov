
# coding: utf-8

# In[212]:


from urllib.request import urlretrieve
import vk, os, time, math, vk_api

import vk_api


def main():

    login, password = '+79119781349', 'Zenit1984'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    
if __name__ == '__main__':
    main()

main_request = input('Ссылка пользователя - ')
main_request = main_request.split('/')
screenname = main_request[-1]
print(screenname)

id_get = vkapi.account.getProfileInfo(v=5.95)
print(id_get)

owner_id = 2943984

user_get = vkapi.users.get(user_id = owner_id, v=5.95)
print(user_get)
firstname = user_get[0].get('first_name')
lastname = user_get[0].get('last_name')

def Download_photo(X):
    counter = 0 # текущий счетчик
    prog = 0 # процент загруженных
    breaked = 0 # не загружено из-за ошибки
    time_now = time.time() # время старта
    
    if not os.path.exists('saved_from_VK'):
        os.mkdir('saved_from_VK')
    
    photo_folder = 'saved/{0}_{1}_{2}'.format(lastname, firstname, X)
    if not os.path.exists(photo_folder):
        os.mkdir(photo_folder)
   
    for j in range(len(photos_count.get('items'))): # Подсчитаем&nbsp;сколько раз нужно получать список фото, так как число получится не целое - округляем в большую сторону

        photos = vkapi.photos.get(owner_id=owner_id, album_id = X, count=1000, offset=j*1000, v = 5.95) #&nbsp;Получаем список фото
        a = photos.get('items')
        for photo in range(len(a)):
            counter += 1

            b = a[photo].get('sizes')
            url = b[-1].get('url')
            print('Загружаю фото № {} из {}. Прогресс: {} %'.format(counter, len(a), prog))
            #print(url)
            prog = round(100/len(a)*counter,2)

            try:
                urlretrieve(url, photo_folder + "/" + os.path.split(url)[1]) # Загружаем и сохраняем файл
            except Exception:
                    print('Произошла ошибка, файл пропущен.')
                    breaked += 1
                    continue
    else:
        print("Все фото загружены.")
'''
photos_count = vkapi.photos.getAlbums(owner_id=owner_id, v = 5.95)
#print(photos_count)
#print('\n')
list_Albums = []

a = photos_count.get('items')
print(a)
for t in a:
    b = t.get('id')
    list_Albums.append(str(b))
print(list_Albums)
for albums in list_Albums:
    try:
        Download_photo(albums)
    except:
        continue
'''   
    


# ### 
