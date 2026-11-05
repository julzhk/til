Dev containers in JetBrains is a thing.
-

TIL you can use [dev containers](https://www.jetbrains.com/help/pycharm/start-dev-container-from-scratch.html) in JetBrains IDEs. 

### What's a dev container? 
It's a typical set up these days to make a docker container for your dev env. If not a docker container, then a docker compose - then there's a dev container with the code dependencies as well as 
any other requirements. Maybe a database, redis cache and whatever else you need.

Some troubles with this: the developer requirements are a super-set of the production requirements.

Often the docker compose file is a parallel construction to the deployment infrastucture, which is obviously a duplicative effort and can be out-of-step with the production environment - precisely the scenario using containers was designed to solve.

### Dev containers are an attempt to solve this problem.

Imagine a file that is an extension of your production Dockerfile, but also contains all the IDE plugins, development dependencies, ENV variables and so on: a file that enables a 'click-and-go' development setup.

That's the goal of a dev container configuration file.

[Docker Container: but for your dev env
](https://www.jetbrains.com/help/idea/connect-to-devcontainer.html#dev_container_scenarios)

Example project : [github/idea-demo-devcontainers](https://github.com/IdeaUJetBrains/idea-demo-devcontainers)

---

They appear to have been developed by/for VSCode and Jetbrains is playing catch-up and now supporting them. 

In practice, using dev containers isolates the IDE from the rest of the host system. More: secure, repeatable, & consistent..

---

The downside is that it's a bit more work to set up and the documentation is a bit terse, especially for using them with JetBrains.

FWIW: & here's what they look like: an example dev container config file that uses a docker compose file:

```json
// Info https://containers.dev/implementors/json_reference/
{
  "dockerComposeFile": "docker-compose.yml",
  "service": "devcontainer",
  "workspaceFolder": "/workspaces/${localWorkspaceFolderBasename}",
  "customizations": {
    "jetbrains": {
      "plugins": [
        "org.intellij.plugins.10650-json-parser-and-code-generation",
      ],
      "settings": {
        "com.intellij:app:BuiltInServerOptions.builtInServerPort": 56165,
        "com.intellij:app:HttpConfigurable.use_proxy_pac": true,
        "com.intellij:app:EditorSettings.soft_wrap_file_masks": "*.md; *.txt; *.rst; *.adoc",
        "Git4Idea:app:Git-Application-Settings.use_credential_helper": true,
        "com.intellij:app:Vcs-Log-App-Settings.show_changes_from_parents": true,
        "com.intellij:app:BaseRefactoringSettings.safe_delete_when_delete": false,
        "com.intellij:app:BaseRefactoringSettings.rename_search_in_comments_for_file": false,
        "com.intellij:app:BaseRefactoringSettings.rename_search_for_text_for_file": false,
        "com.intellij:app:BaseRefactoringSettings.rename_search_for_references_for_file": false,
        "com.intellij:app:BaseRefactoringSettings.rename_search_for_references_for_directory": false,
        "com.intellij.database:app:DatabaseSettings.enable-local-filter-by-default": false,
        "com.intellij:app:UsageViewSettings.is_preview_usages": false
      }
    }
  }
}
```