Name     : jdk-osgi-annotation
Version  : sources
Release  : 1
URL      : http://repo1.maven.org/maven2/org/osgi/osgi.annotation/6.0.0/osgi.annotation-6.0.0-sources.jar
Source0  : http://repo1.maven.org/maven2/org/osgi/osgi.annotation/6.0.0/osgi.annotation-6.0.0-sources.jar
Source1  : http://repo1.maven.org/maven2/org/osgi/osgi.annotation/6.0.0/osgi.annotation-6.0.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-osgi-annotation-data
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-aqute-bndlib
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-cglib
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-parent
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-easymock3
BuildRequires : jdk-eclipse-eclipse
BuildRequires : jdk-eclipse-osgi
BuildRequires : jdk-eclipse-osgi-services
BuildRequires : jdk-felix
BuildRequires : jdk-felix-bundlerepository
BuildRequires : jdk-felix-framework
BuildRequires : jdk-felix-osgi-foundation
BuildRequires : jdk-felix-utils
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-kxml
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-bundle-plugin
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-objenesis
BuildRequires : jdk-osgi-compendium
BuildRequires : jdk-osgi-core
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : jdk-xz
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Buildrequires : apache-maven

%description
No detailed description available

%package data
Summary: data components for the jdk-osgi-annotation package.
Group: Data

%description data
data components for the jdk-osgi-annotation package.


%prep 
%setup -c -q
mkdir -p src/main/resources && mv about.html src/main/resources
mkdir -p src/main/java && mv org src/main/java
cp -p %{SOURCE1} pom.xml

# Ensure OSGi metadata is generated
python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject pom:project "

  <packaging>bundle</packaging>
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <Bundle-Name>\${project.artifactId}</Bundle-Name>
            <Bundle-SymbolicName>\${project.artifactId}</Bundle-SymbolicName>
          </instructions>
        </configuration>
      </plugin>
    </plugins>
    </build>"

# Known by two names in maven central, so add an alias for the older name
python3 /usr/share/java-utils/mvn_alias.py org.osgi:osgi.annotation org.osgi:org.osgi.annotation

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n osgi-annotation -d %{buildroot}


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/osgi-annotation/osgi.annotation.jar
/usr/share/maven-metadata/osgi-annotation.xml
/usr/share/maven-poms/osgi-annotation/osgi.annotation.pom
