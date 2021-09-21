from rest_framework import serializers
from apps.users.models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def to_representation(self,instance):
        #data = super().to_representation(instance)
        return {
            'id': instance['id'],
            'nombre_usuario': instance['username'],
            'correo_electronico': instance['email'],
            'clave': instance['password']
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()
    
    def validate_name(self,value):
        # custom validation
        if 'developer' in value:
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')
        return value

    def validate_email(self,value):
        # custom validation
        if value == '':
            raise serializers.ValidationError('Tiene que indicar un correo')

        return value

    def validate(self,data):
        return data
    
    def create(self,validated_data):
        return User.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance
    
    """ def save(self):
        print(self.validated_data) """