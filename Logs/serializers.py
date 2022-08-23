from rest_framework import serializers,exceptions
from .models import log



class Createlog_Serializer(serializers.Serializer):
    time_stamp = serializers.DateTimeField()

    def validate(self, attrs):
        user = self.context["user_request"]
        if log.objects.filter(type=False, user=user, time_stamp=attrs['time_stamp']).first() is not None:
            raise serializers.ValidationError("Already Exists!")
        user_file = log.objects.create(user=user)
        user_file.type = False
        user_file.time_stamp = attrs['time_stamp']
        user_file.user = user
        last_log = log.objects.filter(user=user,type=False).order_by('-time_stamp')
        if last_log.first() is not None:
            index = -1
            user_file.is_started = True
            for log_value in last_log:
                if attrs['time_stamp'] > log_value.time_stamp:
                    index = log_value.time_stamp
                    user_file.is_started = not log_value.is_started
                    break
            for log_item in last_log:
                if index == -1:
                    log_item.is_started = not log_item.is_started
                    log_item.save()
                elif log_item.time_stamp > index:
                    log_item.is_started = not log_item.is_started
                    log_item.save()
        else:
            user_file.is_started = True
        user_file.save()
        return attrs


class Deletelog_Serializer(serializers.Serializer):
    ID = serializers.IntegerField()

    def validate(self, attrs):
        user = self.context["user_request"]
        try:
            log_to_delete = log.objects.filter(type=False, id=attrs['ID']).first()
        except:
            raise serializers.ValidationError("log not founded!")

        if log_to_delete is not None:
            last_log = log.objects.filter(type=False, user=user).order_by('time_stamp')
            for log_item in last_log:
                if log_item.time_stamp > log_to_delete.time_stamp:
                    log_item.is_started = not log_item.is_started
                    log_item.save()
            log_to_delete.delete()
        else:
            raise serializers.ValidationError("log not founded!")
        return attrs


class Upadatelog_Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    time_stamp = serializers.DateTimeField()

    def validate(self, attrs):
        user = self.context["user_request"]
        if log.objects.filter(type=False, user=user,time_stamp=attrs['time_stamp']).first() is not None:
            raise serializers.ValidationError("You have already logged in this momment and please insert new date and time")
        user = self.context["user_request"]
        try:
            log_to_delete = log.objects.filter(type=False, id=attrs['id']).first()
        except:
            raise serializers.ValidationError("log not founded!")
        if log_to_delete is not None:
            last_log = log.objects.filter(user=user,type=False).order_by('time_stamp')
            for log_item in last_log:
                if log_item.time_stamp > log_to_delete.time_stamp:
                    log_item.is_started = not log_item.is_started
                    log_item.save()
            log_to_delete.delete()
        else:
            raise serializers.ValidationError("log not founded!")
        user_file = log.objects.create(user=user)
        user_file.type = False
        user_file.time_stamp = attrs['time_stamp']
        user_file.user = user
        last_log = log.objects.filter(user=user, type=False).order_by('-time_stamp')
        if last_log.first() is not None:
            index = -1
            user_file.is_started = True
            for log_value in last_log:
                if attrs['time_stamp'] > log_value.time_stamp:
                    index = log_value.time_stamp
                    user_file.is_started = not log_value.is_started
                    break
            for log_item in last_log:
                if index == -1:
                    log_item.is_started = not log_item.is_started
                    log_item.save()
                elif log_item.time_stamp > index:
                    log_item.is_started = not log_item.is_started
                    log_item.save()
        else:
            user_file.is_started = True
        user_file.save()
        return attrs


class CreateLeave_Serializer(serializers.Serializer):
    start_time_stamp = serializers.DateTimeField()
    end_time_stamp = serializers.DateTimeField()

    def validate(self, attrs):
        user = self.context["user_request"]
        if log.objects.filter(type=True, user=user, time_stamp=attrs['start_time_stamp'],is_started=True).first() is not None:
            print("1")
            raise serializers.ValidationError("Incompatibility with previous requests")
        if log.objects.filter(type=True, user=user, time_stamp=attrs['end_time_stamp'],is_started=False).first() is not None:
            print("2")
            raise serializers.ValidationError("Incompatibility with previous requests")
        all_log = log.objects.filter(type=True, user=user)
        for log_item in all_log:
            if log_item.time_stamp < attrs['end_time_stamp'] and log_item.time_stamp > attrs['start_time_stamp']:
                print("3")
                raise serializers.ValidationError("Incompatibility with previous requests")
        last_log = log.objects.filter(user=user,type=True).order_by('-time_stamp')
        for log_value in last_log:
            if attrs['start_time_stamp'] > log_value.time_stamp:
                # print("founded:     ", log_value.time_stamp)
                first_index = log_value
                if first_index.is_started:
                    print("4")
                    raise serializers.ValidationError("Incompatibility with previous requests")
                break
        start_log = log.objects.create(user=user, is_started=True, type=True, time_stamp=attrs['start_time_stamp'])
        end_log = log.objects.create(user=user, is_started=False, type=True, time_stamp=attrs['end_time_stamp'])
        start_log.save()
        end_log.save()
        return attrs


class DeleteLeave_Serializer(serializers.Serializer):
    Start_ID = serializers.IntegerField()
    End_ID = serializers.IntegerField()

    def validate(self, attrs):
        user = self.context["user_request"]
        try:
            log_to_delete = log.objects.filter(type=True, id=attrs['Start_ID'], is_started=True ).first()
            second_log_to_delete = log.objects.filter(type=True, id=attrs['End_ID'], is_started=False ).first()
        except:
            raise serializers.ValidationError("log not founded!")

        if log_to_delete and second_log_to_delete is not None:
            log_to_delete.delete()
            second_log_to_delete.delete()
        else:
            raise serializers.ValidationError("log not founded!")
        return attrs

















