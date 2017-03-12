/*
 * formulaire.c
 *
 * Philippe Dax - sept 1995
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cgi.h>

#define TITRE "Resultat du questionnaire"

cgi_main(cgi_info *ci)
{
	form_entry *parms;
	char *prenom, *nom, *couleur, *choix, *message;	/* parametres */
        
	parms = get_form_entries(ci);	/* lecture des parametres */
        prenom  = parmval(parms, "prenom");
        nom     = parmval(parms, "nom");
        couleur = parmval(parms, "couleur");
        choix   = parmval(parms, "choix");
        message = parmval(parms, "message");
     
	print_mimeheader("text/html");	/* en-tete MIME: type de document */
	printf("<html>\n");
	printf("<head>\n");
	printf("<title>%s</title>\n", TITRE);
	printf("</head>\n");
	printf("<body bgcolor=\"dddddd\">\n");
	printf("<h1>%s</h1>\n", TITRE);
	printf("<hr>\n");

        /*
         * ici commence le traitement
         * ATTENTION: ce processus s'execute sous le controle du serveur httpd
         *            avec l'uid de nobody et non celui de l'utilisateur.
         */
	printf("<b>%s %s</b>, dont la couleur favorite est <b>%s</b>, vous avez répondu <b>%s</b> à la question car vous pensez que :<p><b>%s</b>\n",
		prenom, nom, couleur, choix, message);

        /*
         * ici se termine le traitement
         */
	printf("<hr>\n");
	printf("</body>\n");
	printf("</html>\n");

	free_form_entries(parms);