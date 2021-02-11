from rest_framework import serializers
from Courses.models import Course,Week,Video,Dairy,DairyLabel
class Dairy_label(serializers.ModelSerializer):
    class Meta:
        model = DairyLabel
        fields = '__all__'
class Dairy_S(serializers.ModelSerializer):
    Dairy_label=serializers.StringRelatedField()
    class Meta:
        model=Dairy
        fields= '__all__'
        ordering=["Date"]


class Video_S(serializers.ModelSerializer):
    Dairy=Dairy_S(many=True, read_only=True)
    class Meta:
        model=Video
        fields=["id",
                "Video_URL",
                "Video_Name",
        "Video_Description",
        "Dairy_Description",
                "Video_week",
                "slug",
                "Dairy"
        ]

class Week_S(serializers.ModelSerializer):
    Video_Week=Video_S(many=True, read_only=True)
    view_status_count = serializers.SerializerMethodField()
    class Meta:
        model=Week
        fields=["id","Week_number","Week_name","Course_Week","Video_Week","view_status","view_status_count"]
    def get_view_status_count(self, instance):
        return instance.view_status.count()

class Week_Status(serializers.ModelSerializer):
        view_status_count = serializers.SerializerMethodField()

        class Meta:
            model = Week
            fields = ["id","view_status", "view_status_count"]

        def get_view_status_count(self, instance):
            return instance.view_status.count()
class Course_S(serializers.ModelSerializer):
    Course_week=Week_S(many=True, read_only=True)
    class Meta:
        model=Course
        fields=["id","Name","Description","Date","slug","image","likes","Course_week"]
class Course_LIST_S(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=["id","Name","Description","Date","slug","image","likes"]