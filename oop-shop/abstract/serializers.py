class BaseSerializer:
    class Meta:
        fields = []
        queryset = []
    
    def serialize_object(self, object_):
        fields = self.Meta.fields
        dict_ = {}
        for field in fields:
            dict_[field] = getattr(object_, field)
        return dict_
    
    def serialize_queryset(self, queryset = None):
        if queryset is None:
            queryset = self.Meta.queryset
        list_ = []
        for obj in queryset:
            dict_ = self.serialize_object(obj)
            list_.append(dict_)
        return list_

    