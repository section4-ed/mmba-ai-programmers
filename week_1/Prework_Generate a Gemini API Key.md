## Generate a Google Gemini API Key

At Section, we want to ensure your work remains yours while giving you hands-on experience with modern AI tools. For this course, you can choose to use Google Gemini instead of OpenAI by setting up your own Gemini API key.

Here's why:

- **Ownership & Privacy**: Using your own API key keeps your work private and under your control.

- **No Upfront Cost**: Gemini offers free access with generous usage limits—plenty for completing this course.

### API Cost & Rate-Limit Awareness

While Gemini currently offers free access, it's important to understand rate limits and request quotas when working with any AI platform. This kind of cost and usage awareness is vital as you plan and advocate for AI at work. You'll gain experience estimating usage, debugging API calls, and monitoring request throughput—skills that help you speak confidently about feasibility, cost, and scalability.

### 1: Create Your Google Account and Get a Gemini API Key

We've written this course using OpenAI, but Gemini's APIs have near feature parity. If you'd like to explore Gemini, follow the steps below:

1. Visit [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

2. Sign in with your Google account and generate an API key

3. Copy and securely store your key—you'll need it to access the Gemini API throughout the course

### 2: Save the API key to an environment variable

To keep your API key secure and separate from your code, save it to an environment variable called `GEMINI_API_KEY`.

<details>

<summary>On Mac:</summary>

- Open your `.bash_profile` or `.zshrc` file: `open ~/.bash_profile` or `open ~/.zshrc`

- Add the line: `export GEMINI_API_KEY={your key}`

- Save and close the file, then run `source ~/.bash_profile` (or `source ~/.zshrc`)

</details>

<details>

<summary>On Windows:</summary>

- Go to "Control Panel" > "System and Security" > "System"

- Click "Advanced system settings"

- Under the "Advanced" tab, click "Environment Variables"

- Click "New" under "User variables"

- Set the variable name as `GEMINI_API_KEY` and paste your key as the value

- Click "OK" to save

</details>

### Next Steps

That's it! You're now set up to use Gemini for the course. While our sample code uses OpenAI, you can adapt it to Gemini using [Google's Gemini API docs](https://ai.google.dev/docs). The underlying concepts remain the same.
