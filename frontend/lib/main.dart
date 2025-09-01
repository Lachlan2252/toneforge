import 'package:flutter/material.dart';

void main() {
  runApp(const ToneForgeApp());
}

class ToneForgeApp extends StatelessWidget {
  const ToneForgeApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ToneForge',
      home: Scaffold(
        appBar: AppBar(title: const Text('ToneForge')),
        body: const Center(child: Text('Welcome to ToneForge')),
      ),
    );
  }
}
