from django.test import TestCase

from answers.models import Answer


class CreateAnswerViewTest(TestCase):
    def test_create_answer_should_save_models(self):
        response = self.client.post('/create_answer_class/', data = {
            'text': 'yes',
            'image': 'https://media1.giphy.com/media/fw8g5zvVepbal1w6KT/giphy.webp'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/answer/')

        answer = Answer.objects.last()

        self.assertEqual(answer.text, 'yes')
        self.assertEqual(answer.image, 'https://media1.giphy.com/media/fw8g5zvVepbal1w6KT/giphy.webp')
        