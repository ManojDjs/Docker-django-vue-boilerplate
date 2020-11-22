from rest_framework import serializers
from Programs.models import ISQ_Questions,ISQAnswer,Initial_ISQ

class Question_S(serializers.ModelSerializer):
    class Meta:
        model=ISQ_Questions
        fields='__all__'
class Answer_S(serializers.ModelSerializer):
    class Meta:
        model=ISQAnswer
        fields='__all__'

class TotalAnswers_A(serializers.ModelSerializer):
    ISQ=Answer_S(many=True,read_only=True)
    total_questions=serializers.SerializerMethodField()
    total_answers=serializers.SerializerMethodField()

    class Meta:
        model=Initial_ISQ
        fields=('Answered_by','ISQ','total_answers','total_questions')
    def get_total_answers(self,instance):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            print(user)
        print(serializers.CurrentUserDefault())
        u=[u for u in ISQAnswer.objects.filter(answer_by=user)]
        return len(u)

    def get_total_questions(self, instance):

        u = [u for u in ISQ_Questions.objects.all()]
        return len(u)

# class Posts_S(serializers.Serializer):
#     post_text=serializers.CharField(max_length=5000)
#     active = serializers.BooleanField(default=True)
#     created = serializers.DateTimeField(read_only=True)
#     updated = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return Posts.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.post=validated_data.get('post',instance.post)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance