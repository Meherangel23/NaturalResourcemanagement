import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

interface ChatMessage {
  text: string;
  sender: 'user' | 'bot';
}

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.scss']
})
export class ChatbotComponent implements OnInit {

  messages: ChatMessage[] = [];
  message: string = '';
  isMinimized: boolean = true;
  isMaximized: boolean = false;
  isClosed: boolean = false;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  sendMessage() {
    if (this.message.trim() === '') return;

    this.messages.push({ text: this.message, sender: 'user' });

    this.http.post<any>(environment.apiUrl + '/chatbot/message', { text: this.message })
      .subscribe(response => {
        this.messages.push({ text: response.reply, sender: 'bot' });
      });

    this.message = '';
  }

  minimize() {
    this.isMinimized = !this.isMinimized;
    this.isMaximized = false;
  }

  maximize() {
    this.isMaximized = !this.isMaximized;
    this.isMinimized = false;
  }

  close() {
    this.isClosed = true;
  }
}