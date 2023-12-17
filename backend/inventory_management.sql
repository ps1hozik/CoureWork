CREATE TABLE public.users (
	"id" serial NOT NULL,
	"name" varchar(128) NOT NULL,
	"login" varchar(20) NOT NULL UNIQUE,
	"hashed_password" varchar NOT NULL,
	"post" varchar(255) NOT NULL,
	"organization_id" integer,
	"warehouse_id" integer,
	CONSTRAINT "users_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);
CREATE INDEX users_id_index ON users (id);


CREATE TABLE public.organizations (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"code" varchar NOT NULL UNIQUE,
	"description" varchar,
	"count_of_warehouses" integer NOT NULL DEFAULT 0,
	"manager_id" integer NOT NULL,
	CONSTRAINT "organizations_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);
CREATE INDEX organizations_id_index ON organizations (id);


CREATE TABLE public.warehouses (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"description" varchar,
	"address" varchar NOT NULL,
	"count_of_employees" integer NOT NULL DEFAULT 0,
	"product_quantity" integer NOT NULL DEFAULT 0,
	"organization_id" integer NOT NULL,
	CONSTRAINT "warehouses_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);
CREATE INDEX warehouses_id_index ON warehouses (id);


CREATE TABLE public.products (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"manufacturer" varchar(255) NOT NULL,
	"barcode" integer,
	"description" varchar,
	"price" DECIMAL NOT NULL,
	"total_quantity" integer NOT NULL,
	"booked_quantity" integer,
	"created_at" DATETIME NOT NULL DEFAULT NOW()::timestamp,
	"updated_at" DATETIME NOT NULL DEFAULT NOW()::timestamp,
	"last_employee_id" integer NOT NULL,
	"warehouse_id" integer NOT NULL,
	CONSTRAINT "products_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);
CREATE INDEX products_id_index ON products (id);
CREATE INDEX products_manufacturer_index ON products (manufacturer);


CREATE TABLE public.roles (
	"id" serial NOT NULL,
	"name" varchar(128) NOT NULL UNIQUE,
	"user_id" integer NOT NULL,
	CONSTRAINT "roles_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);
CREATE INDEX roles_id_index ON roles (id);
CREATE INDEX roles_name_index ON roles (name);


ALTER TABLE "users" ADD CONSTRAINT "users_fk0" FOREIGN KEY ("organization_id") REFERENCES "organizations"("id") ON DELETE SET NULL;
ALTER TABLE "users" ADD CONSTRAINT "users_fk1" FOREIGN KEY ("warehouse_id") REFERENCES "warehouses"("id") ON DELETE SET NULL;

ALTER TABLE "organizations" ADD CONSTRAINT "organizations_fk0" FOREIGN KEY ("manager_id") REFERENCES "users"("id");

ALTER TABLE "warehouses" ADD CONSTRAINT "warehouses_fk0" FOREIGN KEY ("organization_id") REFERENCES "organizations"("id");

ALTER TABLE "products" ADD CONSTRAINT "products_fk0" FOREIGN KEY ("last_employee_id") REFERENCES "users"("id");
ALTER TABLE "products" ADD CONSTRAINT "products_fk1" FOREIGN KEY ("warehouse_id") REFERENCES "warehouses"("id");

ALTER TABLE "roles" ADD CONSTRAINT "roles_fk0" FOREIGN KEY ("user_id") REFERENCES "users"("id");






