from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    user_name: Mapped[str] = mapped_column(nullable=False)

    #relationships
    favorites_characters: Mapped[List["Favorite_character"]] = relationship(back_populates="user_favorites_character")
    favorites_planets: Mapped[List["Favorite_planet"]] = relationship(back_populates="user_favorites_planet")
    favorites_films: Mapped[List["Favorite_film"]] = relationship(back_populates="user_favorites_film")
    favorites_vehicles: Mapped[List["Favorite_vehicle"]] = relationship(back_populates="user_favorites_vehicle")
    favorites_species: Mapped[List["Favorite_specie"]] = relationship(back_populates="user_favorites_specie")


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_name": self.user_name
        }
    

class Character(db.Model):
    __tablename__ = "character"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    imageLink: Mapped[str] = mapped_column(nullable=False)

    #relationships
    characters: Mapped[List["Favorite_character"]] = relationship(back_populates="favorite_character")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "imageLink": self.imageLink
        }
    
class Planet(db.Model):
    __tablename__ = "planet"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    imageLink: Mapped[str] = mapped_column(nullable=False)

    #relationships
    planets: Mapped[List["Favorite_planet"]] = relationship(back_populates="planet_favorite")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "imageLink": self.imageLink
        }

class Film(db.Model):
    __tablename__ = "film"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    imageLink: Mapped[str] = mapped_column(nullable=False)

    #relationships
    films: Mapped[List["Favorite_film"]] = relationship(back_populates="film_favorite")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "imageLink": self.imageLink
        }
    
class Vehicle(db.Model):
    __tablename__ = "vehicle"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    imageLink: Mapped[str] = mapped_column(nullable=False)

    #relationships
    vehicles: Mapped[List["Favorite_vehicle"]] = relationship(back_populates="vehicle_favorite")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "imageLink": self.imageLink
        }
    
class Specie(db.Model):
    __tablename__ = "specie"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    imageLink: Mapped[str] = mapped_column(nullable=False)

    #relationships
    species: Mapped[List["Favorite_specie"]] = relationship(back_populates="specie_favorite")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "imageLink": self.imageLink
        }
    
#Favoritos

class Favorite_character(db.Model):
    __tablename__ = "favorite_character"

    id: Mapped[int] = mapped_column(primary_key=True)

    #foreign keys
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable = False)
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"),nullable = False)

    #relationships
    user_favorites_character: Mapped["User"] = relationship(back_populates="favorites_characters")
    favorite_character: Mapped["Character"] = relationship(back_populates="characters")


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }  

class Favorite_planet(db.Model):
    __tablename__ = "favorite_planet"

    id: Mapped[int] = mapped_column(primary_key=True)


    #foreign keys
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable = False)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable = False)

    #relationships
    user_favorites_planet: Mapped["User"] = relationship(back_populates="favorites_planets")
    planet_favorite: Mapped["Planet"] = relationship(back_populates="planets")


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }
    
class Favorite_film(db.Model):
    __tablename__ = "favorite_film"

    id: Mapped[int] = mapped_column(primary_key=True)


    #foreign keys
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable = False)
    film_id: Mapped[int] = mapped_column(ForeignKey("film.id"), nullable = False)

    #relationships
    user_favorites_film: Mapped["User"] = relationship(back_populates="favorites_films")
    film_favorite: Mapped["Film"] = relationship(back_populates="films")


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "film_id": self.film_id
        }
    
class Favorite_vehicle(db.Model):
    __tablename__ = "favorite_vehicle"

    id: Mapped[int] = mapped_column(primary_key=True)


    #foreign keys
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable = False)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicle.id"), nullable = False)

    #relationships
    user_favorites_vehicle: Mapped["User"] = relationship(back_populates="favorites_vehicles")
    vehicle_favorite: Mapped["Vehicle"] = relationship(back_populates="vehicles")


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id
        }
    
class Favorite_specie(db.Model):
    __tablename__ = "favorite_specie"

    id: Mapped[int] = mapped_column(primary_key=True)


    #foreign keys
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable = False)
    specie_id: Mapped[int] = mapped_column(ForeignKey("specie.id"), nullable = False)

    user_favorites_specie: Mapped["User"] = relationship(back_populates="favorites_species")
    specie_favorite: Mapped["Specie"] = relationship(back_populates="species")


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "specie_id": self.specie_id
        }