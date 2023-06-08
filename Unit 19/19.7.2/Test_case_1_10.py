def test_fail_get_api_key_for_invalid_user(email=valid_email, password='12345'):
    """ Проверяем что запрос api ключа возвращает статус 403 и в результате не содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result
    
    
def test_fail_get_all_pets_with_invalid_key(filter=''):
    """ Проверяем что запрос всех питомцев не возвращает список.
    При неверном api ключе."""

    auth_key = invalid_auth_key

    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 403
    
    
def test_fail_add_new_pet_with_invalid_data(name='Вася', animal_type='двортерьер',
                                          age='Вася', pet_photo='images/dog.jpeg'):
    """Проверяем что нельзя добавить питомца с не корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400 
    
    
def test_fail_add_new_pet_with_invalid_data_max(name='Вася', animal_type='двортерьер',
                                          age='6gsIRL785017xWaKe24301a72Ios484a4651K1q2a1GX3154934Noi2K34I34M9j6gsIRL785017xWaKe24301a72Ios484a4651K1q2a1GX3154934Noi2K34I34M9j',
                                                pet_photo='images/dog.jpeg'):
    """Проверяем что можно добавить питомца с не корректными большими данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    
    
def test_fail_add_new_pet_with_invalid_data_empty(name='', animal_type='', age='', pet_photo='images/dog.jpeg'):
    """Проверяем что можно добавить питомца с не корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400

    
def test_fail_add_new_pet_with_invalid_photo(name='Вася', animal_type='двортерьер',
                                            age='Вася', pet_photo='images/Fail.txt'):
    """Проверяем что можно добавить питомца с текстовый файлом вместо изображения"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    
    
def test_successful_update_self_pet_photo(pet_photo='images/cow.jpg'):
    """Проверяем возможность обновления фото питомца"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его фото
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        # assert result['pet_photo'] == pet_photo
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
        
        
def test_add_new_pet_nophoto_with_valid_data(name='Барсик>', animal_type='Сиамский', age='5'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_nophoto(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
    
def test_fail_delete_self_pet():
    """Проверяем возможность удаления питомца с неверным ключом"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    auth_key = invalid_auth_key
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 403
    assert status == 403
    
    
def test_fail_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце с неверным auth_key"""

    # Получаем ключ auth_key и список своих питомцев
    auth_key = invalid_auth_key
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 403
        assert status == 403
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
