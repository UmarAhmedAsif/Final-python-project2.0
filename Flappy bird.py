import 'package:flutter/material.dart';
import 'package:flame/game.dart';
import 'package:flame/components.dart';
import 'package:flame/flame.dart';
import 'dart:ui';

void main() {
  runApp(GameWidget(game: FlappyBird()));
}

class FlappyBird extends FlameGame {
  late Bird _bird;
  late double screenHeight;
  late double screenWidth;
  late double birdHeight;
  late double birdWidth;
  
  @override
  Future<void> onLoad() async {
    screenHeight = size.y;
    screenWidth = size.x;
    birdHeight = 50;
    birdWidth = 50;
    
    // Load the bird
    _bird = Bird(position: Vector2(screenWidth / 4, screenHeight / 2));
    add(_bird);
  }

  @override
  void update(double dt) {
    super.update(dt);
    _bird.update(dt);
  }

  @override
  void render(Canvas canvas) {
    super.render(canvas);
    _bird.render(canvas);
  }
}

class Bird extends PositionComponent with HasGameRef {
  double velocity = 0;
  double gravity = 0.2;
  double lift = -5;
  
  Bird({required Vector2 position}) {
    this.position = position;
  }

  @override
  void update(double dt) {
    velocity += gravity;
    position.y += velocity;

    // Prevent the bird from falling below the ground
    if (position.y > gameRef.size.y - 50) {
      position.y = gameRef.size.y - 50;
    }

    // Prevent the bird from flying off the top
    if (position.y < 0) {
      position.y = 0;
    }
  }

  @override
  void onTap() {
    velocity = lift;
  }

  @override
  void render(Canvas canvas) {
    final paint = Paint()..color = Colors.yellow;
    canvas.drawRect(Rect.fromLTWH(position.x, position.y, 50, 50), paint);
  }
}
flutter run

