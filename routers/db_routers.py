class AuthRouter:
    route_app_labels = {'auth', 'contenttypes', 'admin', 'sessions'}

    def db_for_read(self, model, **hints):
        
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def db_for_write(self, model, **hints):
        
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        
        if app_label in self.route_app_labels:
            return db == 'users_db'
        return None


class Tires:
    route_app_labels = {'tires'}

    def db_for_read(self, model, **hints):
        
        if model._meta.app_label in self.route_app_labels:
            return 'tires_db'
        return None

    def db_for_write(self, model, **hints):
        
        if model._meta.app_label in self.route_app_labels:
            return 'tires_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        
        if app_label in self.route_app_labels:
            return db == 'tires_db'
        return None


class Pallets:
    route_app_labels = {'pallets'}

    def db_for_read(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'pallet_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'pallet_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'pallet_db'
        return None
