from rest_framework import status
from rest_framework.test import APIClient
from django.contrib import admin
from django.contrib.auth import get_user_model
import pytest



@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_return_401(self):
        # Arrange

        # Act
        client = APIClient()
        response = client.post('/store/collections/', {'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_if_user_is_authenticated_return_403(self):
        # check if the user is authenticated but not an admin
        User = get_user_model()
        user = User.objects.create_user(username='ali', password='Aliali12..')

        # Arrange
        client = APIClient() # Create an instance of APIClient for testing
        client.force_authenticate(user=user)

        # Act
        response = client.post('/store/collections/', {'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_user_is_admin_return_201(self):
        # check if the user is authenticated but not an admin
        User = get_user_model()
        admin = User.objects.create_user(username='ali', password='Aliali12..', is_staff=True)

        # Arrange
        client = APIClient()
        client.force_authenticate(user=admin)

        # Act
        response = client.post('/store/collections/', {'title': 'a'})
        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == 'a' # check if the title is 'a'


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_return_401(self):
        # Arrange

        # Act
        client = APIClient()
        response = client.post('/store/products/', {'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_if_user_is_authenticated_return_403(self):
        # check if the user is authenticated but not an admin
        User = get_user_model()
        user = User.objects.create_user(username='ali', password='Aliali12..')

        # Arrange
        client = APIClient() # Create an instance of APIClient for testing
        # APIClient is actually used to simulate a client making requests to the API
        # client.login(username='ali', password='Aliali12..')
        client.force_authenticate(user=user)

        # Act
        response = client.post('/store/products/', {'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    # def test_if_user_is_admin_return_201(self):
    #     # check if the user is authenticated but not an admin
    #     User = get_user_model()
    #     admin = User.objects.create_user(username='ali', password='Aliali12..', is_staff=True)

    #     # Arrange
    #     client = APIClient()
    #     # APIClient is actually used to simulate a client making requests to the API   
    #     client.force_authenticate(user=admin) # Create an instance of APIClient for testing
    #     # Act
    #     response = client.post('/store/products/',{
    #         'title': 'a',
    #         'slug': 'a',
    #         'description': 'test product',
    #         'price': 10,
    #         'inventory': 5,
    #         'collection': 4,
    #     })
    #     # Assert
    #     assert response.status_code == status.HTTP_201_CREATED
    #     assert response.data['title'] == 'a' # check if the title is 'a'
        # explanation:
        # - The test checks if the API returns a 201 Created status code
        # and the correct title when a valid request is made to create a product.
        # - The test also checks if the response data contains the correct title.

    
    def test_if_data_is_invalid_return_400(self):
        # admin = UserFactory(is_staff=True)
        User = get_user_model()
        admin = User.objects.create_user(username='admin', password='admin123', is_staff=True)
        client = APIClient()
        client.force_authenticate(user=admin)

        response = client.post('/store/products/', {})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'title' in response.data
    # explanation:
    # - The test checks if the API returns a 400 Bad Request status code 
    # when the request data is invalid (empty in this case).
