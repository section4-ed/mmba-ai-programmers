## Generate an Open AI Key  
At MindBit, we prioritize protecting your intellectual property while ensuring a smooth and cost-effective learning experience. As part of our AI training, we ask each participant to sign up for their own OpenAI API account.

Here's why:  
- IP Protection: By using your own API key, any projects or work you create will remain entirely under your ownership and control.  
- Minimal Costs: Our course only requires about $5 of token usage, so you'll have full transparency and control over your API costs.

### API Cost-Literacy is Critical  
Learning how to use OpenAI's billing tools is very important for helping your company understand the costs of using AI. As you start advocating for AI projects, being able to clearly explain and predict expenses will make a huge difference. It shows that you've done your homework and can back up your ideas with real numbers, making it easier for your company to trust and support your AI plans. Plus, it helps make sure AI use stays within budget and delivers value. 

*We recommend you put $5 into your account* and closely monitor the spend as you go through your projects here to learn how much API usage costs as a hands-on way of learning how to navigate different models, token usage, etc. You can add in more money as you need or not depending on the scope of your project goals. *To get through all the course material should cost around $1, but you may use more if your project requires it.*

Seeing those tokens get used up, monitoring the throughput, and seeing all the dots connect is part of the magic that you will need to explain to your team or leaders.  

### 1: Create Your OpenAI Account  
We are using OpenAI for the duration of this course as it is the most widely used platform in industry. The same concepts we teach here will be applicable to all platforms.

1. Visit [OpenAI API website](https://platform.openai.com/) and sign up for an account if you don't already have one.  
2. Once you have signed up, log in and [navigate to the Billing section](https://platform.openai.com/settings/organization/billing/overview).  
3. Add $5 to your account to cover API usage throughout the course. This amount should be sufficient for the duration of the program.

### 2: Generate Your API Key  
Generating an API key is important because it securely lets your application access the OpenAI API, keeping your usage authorized and data protected.

1. In your OpenAI account, go to the [API Keys section](https://platform.openai.com/api-keys)  
2. Generate a new API key and save it securely somewhere you won't forget. You will use this key to access the API during the course.

### 3: Save the API key to an environment variable  
Saving your API key to an environment variable keeps it secure and hidden from your code. It prevents accidentally sharing sensitive info and keeps your code clean and safe to share with others.

   <details>  
   <summary>On Mac:</summary>

   - Open your `.bash_profile` file with a text editor: `open ~/.bash_profile`  
   - Add the line `export OPENAI_API_KEY={your key}`  
   - Save the file and close it

   </details>

   <details>  
   <summary>On Windows:</summary>

   - Go to "Control Panel" > "System and Security" > "System"  
   - Click "Advanced system settings"  
   - Select the "Advanced" tab and click "Environment Variables"  
   - Under "User variables", click "New"  
   - Enter the variable name as "OPENAI_API_KEY" and the value as your key.  
   - Click "OK" to save

   </details>
