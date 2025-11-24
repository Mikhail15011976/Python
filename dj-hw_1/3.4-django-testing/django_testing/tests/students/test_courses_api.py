import pytest

from students.models import Course

BASE_URL = '/api/v1/courses/'


@pytest.mark.django_db
def test_get_course(client, course_factory, student_factory):

    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=2, students=students)
    url = BASE_URL + str(courses[0].id) + '/'
    response = client.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data['id'] == courses[0].id


@pytest.mark.django_db
def test_get_courses(client, course_factory):

    courses = course_factory(_quantity=10)
    response = client.get(BASE_URL)
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, d in enumerate(data):
        assert d['id'] == courses[i].id


@pytest.mark.django_db
def test_get_course_filter_id(client, course_factory):

    courses = course_factory(_quantity=2)
    url = BASE_URL + '?id=' + str(courses[0].id)
    response = client.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data[0]['id'] == courses[0].id


@pytest.mark.django_db
def test_get_course_filter_name(client, course_factory):
    courses = course_factory(_quantity=10)
    url = BASE_URL + '?name=' + courses[0].name
    response = client.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(client):

    count = Course.objects.count()
    response = client.post(BASE_URL, data={'name': 'Кулинарные курсы'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):

    courses = course_factory(_quantity=10)
    url = BASE_URL + str(courses[0].id) + '/'
    response = client.patch(url, data={'name': 'Курсы по программированию'})
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == 'Курсы по программированию'


@pytest.mark.django_db
def test_delete_course(client, course_factory):

    courses = course_factory(_quantity=10)
    count = Course.objects.count()
    url = BASE_URL + str(courses[0].id) + '/'
    response = client.delete(url)

    assert response.status_code == 204
    assert Course.objects.count() == count - 1
