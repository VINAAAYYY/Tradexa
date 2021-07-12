class AuthRouter():
    route_app_labels = {'Products', 'sessions', 'admin'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'products_db'
        return None

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'products_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'products_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
            return True
        return None