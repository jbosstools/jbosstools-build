from github import Github
import sys
import semantic_version

g = Github(sys.argv[1], sys.argv[2])

org = g.get_organization("jbosstools")

#repos not following jbt tagging cycle
nondevrepos = [
    "jbosstools-gwt",
    "jbosstools-deltacloud",
    "jbosstools-fuse-extras",
    "jbosstools-devdoc",
    "jbosstools-locus",
    "jbosstools-runtime-soa",
    "jbosstools-maven-plugins",
    "jbosstools-jbpm",
    "jbosstools-esb",
    "jbosstools-documentation",
    "jbosstools-full-svn-mirror",
    "jbosstools-website",
    "m2e-apt",
    "m2e-wro4j",
    "m2e-jdt-compiler",
    "m2e-wtp-tests",
    "jbosstools-integration-tests",
     "jbosstools-integration-stack",
    "jboss-wfk-quickstarts",
    "jbosstools-playground",
    "contacts-mobile-basic-cordova",
    "m2e-polyglot-poc",
    "jbosstools-bpel",
    "jbosstools-integration-stack-tests",
    "jbosstools-xulrunner",
    "jbosstools-install-rinder",
    "jbosstools-target-platforms",
    "jbosstools-central-webpage", ## remove when part of release?
    "incubator-ripple", ## this should be tagged somehow, but how ?
    "jbosstools-versionwatch",
    "jbosstools-archetypes",
    "jbosstools-install-grinder"
    ]

since = {
    "jbosstools-base" : "",
    "jbosstools-birt" : "jbosstools-4",
    "jbosstools-build" : "jbosstools-4",
    "jbosstools-build-ci" : "jbosstools-4",
    "jbosstools-build-sites" : "jbosstools-4",
    "jbosstools-central" : "jbosstools-4",
    "jbosstools-download.jboss.org" : "jbosstools-4",
    "jbosstools-forge" : "jbosstools-4.1",
    "jbosstools-javaee" : "",
    "jbosstools-jst" : "",
    "jbosstools-openshift" : "jbosstools-4.1",
    "jbosstools-portlet" : "jbosstools-4",
    "jbosstools-server" : "",
    "jbosstools-vpe" : "",
    "jbosstools-webservices" : "jbosstools-4",
    "jbosstools-freemarker" : "",
    "jbosstools-hibernate" : "",
    "jbosstools-aerogear" : "jbosstools-4.1.0.Alpha2",
    "jbosstools-discovery" : "jbosstools-4",
    "jbosstools-livereload" : "jbosstools-4.2",
    "jbosstools-arquillian" : "jbosstools-4.2",
    "jbosstools-browsersim" : "jbosstools-4.2.0.Beta1"
}
    
therepo = org.get_repo("jbosstools-base")
thetags = []

for tag in therepo.get_tags():
    if tag.name.startswith("jbosstools"):
        thetags.append(tag.name)

thetags.sort()


print "Checking each repo for diff to base repo"

for repo in org.get_repos():
    if repo.name not in nondevrepos:
        tags = repo.get_tags()
        rawtags = []
        for tag in tags:
            rawtags.append(tag.name)

        sincetags = [e for e in thetags if e > since[repo.name]]
        diff = set(sincetags) - set(rawtags)
        if diff:
            print repo.name + " missing " + str(len(diff)) + " tags"
#            print "\n" + repo.name + " missing tags: \n  " + ",\n  ".join(sorted(diff))
        
 
