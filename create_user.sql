BEGIN;
--
-- Create model User
--
ALTER TABLE auth_user RENAME TO user_user;
ALTER TABLE user_user ADD COLUMN "sso_contact_email" varchar(254) NULL;
--
-- Create model HistoricalUser
--
CREATE TABLE "user_historicaluser" ("id" integer NOT NULL, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL, "first_name" varchar(30) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL, "sso_contact_email" varchar(254) NULL, "history_id" serial NOT NULL PRIMARY KEY, "history_date" timestamp with time zone NOT NULL, "history_change_reason" varchar(100) NULL, "history_type" varchar(1) NOT NULL, "history_user_id" integer NULL);
ALTER TABLE "user_historicaluser" ADD CONSTRAINT "user_historicaluser_history_user_id_18e3a3af_fk_user_user_id" FOREIGN KEY ("history_user_id") REFERENCES "user_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "user_historicaluser_id_9b3a3bdc" ON "user_historicaluser" ("id");
CREATE INDEX "user_historicaluser_username_87870a80" ON "user_historicaluser" ("username");
CREATE INDEX "user_historicaluser_username_87870a80_like" ON "user_historicaluser" ("username" varchar_pattern_ops);
CREATE INDEX "user_historicaluser_history_user_id_18e3a3af" ON "user_historicaluser" ("history_user_id");

INSERT INTO public.django_migrations(app, name, applied)
	VALUES ('user', '0001_initial', now());


COMMIT;



