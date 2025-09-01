# How to Run BQ MCP Server Locally

## 1. Install MCP Toolbox
Install the [MCP Toolbox](https://googleapis.github.io/genai-toolbox/) using Homebrew:
```bash
brew install mcp-toolbox
```

## 2. Install Google Cloud CLI
Download and install the Google Cloud CLI by following the instructions at:
[Google Cloud CLI Installation](https://cloud.google.com/sdk/docs/install)

## 3. Authenticate with Google Account for Local CLI Usage
Set up Application Default Credentials (ADC) for local development:
[Set Up ADC for Local Development](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment)

Run the following command to log in:
```bash
gcloud auth application-default login
```

## 4. Create Tools Configuration File
Create a [`tools.yaml`](./tools.yaml) file for the MCP Server. Refer to the documentation for details:
[BigQuery Tools Configuration](https://googleapis.github.io/genai-toolbox/resources/tools/bigquery/)

## 5. Run MCP Server Locally
Start the MCP Server with the configuration file:
```bash
toolbox --tools-file "tools.yaml"
```

### 5.1 Run MCP Server with UI
To enable the UI, include the `--ui` flag:
```bash
toolbox --tools-file "tools.yaml" --ui
```

## 6. Install MCP Inspector
Install the MCP Inspector tool:
[MCP Inspector GitHub](https://github.com/modelcontextprotocol/inspector)

Run the following command to install and run:
```bash
npx @modelcontextprotocol/inspector
```

## 7. Connect MCP Inspector to Your MCP Server
1. After running the inspector, a console output will provide a link with a token. Open this link in your browser to access the UI.
2. In the web interface, select **Streamable HTTP** as the Transport Type.
3. Enter `http://127.0.0.1:5000/mcp` as the URL.
4. Click the **Connect** button.
5. Verify the connection by pulling the list of tables to ensure everything is functioning correctly.
6. PROFIT!
