from rest_framework import serializers
from MentalWellbeing.models import MWB_Questions,MWB_answers,MWB

class Question_S(serializers.ModelSerializer):
    class Meta:
        model=MWB_Questions
        fields='__all__'
class Answer_S(serializers.ModelSerializer):
    # question_name=Question_S()
    # main_question_set=serializers.StringRelatedField()
    # answer_by=serializers.StringRelatedField()
    class Meta:
        model=MWB_answers
        fields=("id","answer","main_question_set","question_name","answer_by",)

class Answer_Eoboration(serializers.ModelSerializer):
    question_name=Question_S()
    class Meta:
        model=MWB_answers
        fields=("id","answer","main_question_set","question_name","answer_by",)
    # def get_question_type(self):


class TotalAnswers_A(serializers.ModelSerializer):
    MWB=Answer_Eoboration(many=True,read_only=True)
    total_questions=serializers.SerializerMethodField()
    total_answers=serializers.SerializerMethodField()

    class Meta:
        model=MWB
        fields=('id','Answered_by','MWB','total_answers','total_questions')
    def get_total_answers(self,instance):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            print(user)
        print(serializers.CurrentUserDefault())
        u=[u for u in MWB_answers.objects.filter(answer_by=user)]
        return len(u)

    def get_total_questions(self, instance):

        u = [u for u in MWB_Questions.objects.all()]
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