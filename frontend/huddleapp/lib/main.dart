import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.amber,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class Account {
  final int id;
  final String username;
  final String firstname;
  final String lastname;
  final String email;
  Account(this.id, this.username, this.firstname, this.lastname, this.email);
}

class Event {
  final String name;
  final Account account;
}

class _MyHomePageState extends State<MyHomePage> {
  String event_name = "";
  void add_card() async {
    final url = Uri.parse("http://127.0.0.1:8000/events/");
    final response = await http.get(url);
    setState(() {
      event_name = response.body;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("honk")),
      body: Column(
        children: const [
          Card(
            child: ListTile(
              title: Text("Hello"),
            ),
          ),
        ],
      ),
    );
  }
}
