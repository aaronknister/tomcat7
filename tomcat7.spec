# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global jspspec 2.2
%global major_version 7
%global minor_version 0
%global micro_version 52
%global packdname apache-tomcat-%{version}-src
%global servletspec 3.0
%global elspec 2.2
%global tcuid 91

%define package_name tomcat7

# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global basedir %{_var}/lib/%{package_name}
%global appdir %{basedir}/webapps
%global homedir %{_datadir}/%{package_name}
%global bindir %{homedir}/bin
%global confdir %{_sysconfdir}/%{package_name}
%global libdir %{_javadir}/%{package_name}
%global logdir %{_var}/log/%{package_name}
%global cachedir %{_var}/cache/%{package_name}
%global tempdir %{cachedir}/temp
%global workdir %{cachedir}/work
%global _initrddir %{_sysconfdir}/init.d

Name:          %{package_name}
Epoch:         0
Version:       %{major_version}.%{minor_version}.%{micro_version}
Release:       2%{?dist}
Summary:       Apache Servlet/JSP Engine, RI for Servlet %{servletspec}/JSP %{jspspec} API

Group:         System Environment/Daemons
License:       ASL 2.0
URL:           http://tomcat.apache.org/
Source0:       http://www.apache.org/dist/tomcat/tomcat-%{major_version}/v%{version}/src/%{packdname}.tar.gz
Source1:       %{package_name}-%{major_version}.%{minor_version}.conf
Source3:       %{package_name}-%{major_version}.%{minor_version}.sysconfig
Source4:       %{package_name}-%{major_version}.%{minor_version}.wrapper
Source5:       %{package_name}-%{major_version}.%{minor_version}.logrotate
Source6:       %{package_name}-%{major_version}.%{minor_version}-digest.script
Source7:       %{package_name}-%{major_version}.%{minor_version}-tool-wrapper.script
Source8:       servlet-api-OSGi-MANIFEST.MF
Source9:       jsp-api-OSGi-MANIFEST.MF
Source10:      %{package_name}-%{major_version}.%{minor_version}-log4j.properties
Source11:      %{package_name}-%{major_version}.%{minor_version}.init
Source12:      el-api-OSGi-MANIFEST.MF
Source13:      jasper-el-OSGi-MANIFEST.MF
Source14:      jasper-OSGi-MANIFEST.MF
Source15:      tomcat-api-OSGi-MANIFEST.MF
Source16:      tomcat-juli-OSGi-MANIFEST.MF
Source30:      tomcat-preamble
Source31:      tomcat-server
Source32:      tomcat-named.service

Patch0:        %{package_name}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
Patch1:        %{package_name}-%{major_version}.%{minor_version}-tomcat-users-webapp.patch
Patch2:        %{package_name}-%{major_version}.%{minor_version}-remove_nested_restrict.patch
Patch3:        remove-httpcache.patch

BuildArch:     noarch

BuildRequires: ant
BuildRequires: ant-trax
BuildRequires: axis
BuildRequires: findutils
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-daemon
BuildRequires: jakarta-commons-dbcp
BuildRequires: jakarta-commons-pool
BuildRequires: jakarta-taglibs-standard
BuildRequires: java7-devel
BuildRequires: jpackage-utils >= 0:1.7.0
BuildRequires: junit
BuildRequires: log4j
BuildRequires: wsdl4j
BuildRequires: java-openjdk >= 1:1.7.0
Requires:      jakarta-commons-daemon
Requires:      jakarta-commons-logging
Requires:      jakarta-commons-collections
Requires:      jakarta-commons-dbcp
Requires:      jakarta-commons-pool
Requires:      java >= 1:1.6.0
Requires:      jpackage-utils
Requires:      procps
Requires:      %{name}-lib = %{epoch}:%{version}-%{release}
Requires(pre):    shadow-utils
Requires(post):   chkconfig
Requires(preun):  chkconfig
Provides:      %{package_name} = %{epoch}:%{version}-%{release}

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License version 2.0. Tomcat is intended
to be a collaboration of the best-of-breed developers from around the world.

%package admin-webapps
Group: Applications/System
Summary: The host-manager and manager web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Group: Applications/Text
Summary: The docs web application for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description docs-webapp
The docs web application for Apache Tomcat.

%package javadoc
Group: Documentation
Summary: Javadoc generated documentation for Apache Tomcat
Requires: jpackage-utils

%description javadoc
Javadoc generated documentation for Apache Tomcat.

%package jsp-%{jspspec}-api
Group: Development/Libraries
Summary: Apache Tomcat JSP API implementation classes
Provides: jsp = %{jspspec}
Provides: jsp22
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires(post): chkconfig
Requires(postun): chkconfig

%description jsp-%{jspspec}-api
Apache Tomcat JSP API implementation classes.


%package lib
Group: Development/Libraries
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Requires: jakarta-commons-collections
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-pool
Requires(preun): coreutils

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%{servletspec}-api
Group: Development/Libraries
Summary: Apache Tomcat Servlet API implementation classes
Provides: servlet = %{servletspec}
Provides: servlet6
Provides: servlet3
Requires(post): chkconfig
Requires(postun): chkconfig

%description servlet-%{servletspec}-api
Apache Tomcat Servlet API implementation classes.

%package el-%{elspec}-api
Group: Development/Libraries
Summary: Expression Language v1.0 API
Provides: el_1_0_api = %{epoch}:%{version}-%{release}
Provides: el_api = %{elspec}
Requires(post): chkconfig
Requires(postun): chkconfig

%description el-%{elspec}-api
Expression Language 1.0.

%package webapps
Group: Applications/Internet
Summary: The ROOT and examples web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jakarta-taglibs-standard >= 0:1.1

%description webapps
The ROOT and examples web applications for Apache Tomcat.

%prep
%setup -q -n %{packdname}
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
   -name "*.jar" -o -name "*.war" -o -name "*.zip" \) -delete

%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%{__ln_s} $(build-classpath jakarta-taglibs-core) webapps/examples/WEB-INF/lib/jstl.jar
%{__ln_s} $(build-classpath jakarta-taglibs-standard) webapps/examples/WEB-INF/lib/standard.jar

%build
export OPT_JAR_LIST="`cat %{_sysconfdir}/ant.d/trax`"
   # we don't care about the tarballs and we're going to replace
   # tomcat-dbcp.jar with jakarta-commons-{collections,dbcp,pool}-tomcat5.jar
   # so just create a dummy file for later removal
   touch HACK
   %{__mkdir_p} HACKDIR
   touch HACKDIR/build.xml
   # who needs a build.properties file anyway
   %{ant} -Dbase.path="." \
      -Dbuild.compiler="modern" \
      -Dcommons-collections.jar="$(build-classpath jakarta-commons-collections)" \
      -Dcommons-daemon.jar="$(build-classpath jakarta-commons-daemon)" \
      -Dcommons-daemon.native.src.tgz="HACK" \
      -Dtomcat-dbcp.jar="$(build-classpath jakarta-commons-dbcp)" \
      -Dtomcat-native.tar.gz="HACK" \
      -Dtomcat-native.home="." \
      -Dcommons-daemon.native.win.mgr.exe="HACK" \
      -Dnsis.exe="HACK" \
      -Djaxrpc-lib.jar="$(build-classpath axis/jaxrpc)" \
      -Dwsdl4j-lib.jar="$(build-classpath wsdl4j)" \
      -Dcommons-pool.home="HACKDIR" \
      -Dcommons-dbcp.home="HACKDIR" \
      -Dno.build.dbcp=true \
      -Dversion="%{version}" \
      -Dversion.build="%{micro_version}" \
      -Djava.7.home="/usr/lib/jvm/java-1.7.0" \
      deploy dist-prepare dist-source javadoc

    # remove some jars that we'll replace with symlinks later
   %{__rm} output/build/bin/commons-daemon.jar \
           output/build/lib/jakarta-commons-dbcp.jar

    # remove the cruft we created
   %{__rm} output/build/bin/tomcat-native.tar.gz
pushd output/dist/src/webapps/docs/appdev/sample/src
%{__mkdir_p} ../web/WEB-INF/classes
%{javac} -cp ../../../../../../../../output/build/lib/servlet-api.jar -d ../web/WEB-INF/classes mypackage/Hello.java
pushd ../web
%{jar} cf ../../../../../../../../output/build/webapps/docs/appdev/sample/sample.war *
popd
popd

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE8} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/servlet-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/jsp-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE12} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/el-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE13} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/jasper-el.jar META-INF/MANIFEST.MF
cp -p %{SOURCE14} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/jasper.jar META-INF/MANIFEST.MF
cp -p %{SOURCE15} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/tomcat-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE16} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/bin/tomcat-juli.jar META-INF/MANIFEST.MF

%install
# build initial path structure
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sbindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{package_name}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_initrddir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{appdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{bindir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}/Catalina/localhost
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{libdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{logdir}
/bin/touch ${RPM_BUILD_ROOT}%{logdir}/catalina.out
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{_localstatedir}/run
/bin/touch ${RPM_BUILD_ROOT}%{_localstatedir}/run/%{package_name}.pid
/bin/echo "%{package_name}-%{major_version}.%{minor_version}.%{micro_version} RPM installed" >> ${RPM_BUILD_ROOT}%{logdir}/catalina.out
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{homedir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{tempdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{workdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_libexecdir}/%{package_name}

# move things into place
# First copy supporting libs to tomcat lib
pushd output/build
    %{__cp} -a bin/*.{jar,xml} ${RPM_BUILD_ROOT}%{bindir}
    %{__cp} %{SOURCE10} conf/log4j.properties
    %{__cp} -a conf/*.{policy,properties,xml} ${RPM_BUILD_ROOT}%{confdir}
    %{__cp} -a lib/*.jar ${RPM_BUILD_ROOT}%{libdir}
    %{__cp} -a webapps/* ${RPM_BUILD_ROOT}%{appdir}
popd
# javadoc
%{__cp} -a output/dist/webapps/docs/api/* ${RPM_BUILD_ROOT}%{_javadocdir}/%{package_name}

%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE1} \
    > ${RPM_BUILD_ROOT}%{confdir}/%{package_name}.conf
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE3} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{package_name}
%{__install} -m 0644 %{SOURCE4} \
    ${RPM_BUILD_ROOT}%{_sbindir}/%{package_name}
%{__install} -m 0755 %{SOURCE11} \
    ${RPM_BUILD_ROOT}%{_initrddir}/%{package_name}
%{__sed} -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" %{SOURCE5} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{package_name}
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE6} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{package_name}-digest
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE7} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{package_name}-tool-wrapper

%{__install} -m 0755 %{SOURCE30} \
    ${RPM_BUILD_ROOT}%{_libexecdir}/%{package_name}/preamble
%{__install} -m 0755 %{SOURCE31} \
    ${RPM_BUILD_ROOT}%{_libexecdir}/%{package_name}/server

# create jsp and servlet API symlinks
pushd ${RPM_BUILD_ROOT}%{_javadir}
   %{__mv} %{package_name}/jsp-api.jar %{package_name}-jsp-%{jspspec}-api.jar
   %{__ln_s} %{package_name}-jsp-%{jspspec}-api.jar %{package_name}-jsp-api.jar
   %{__mv} %{package_name}/servlet-api.jar %{package_name}-servlet-%{servletspec}-api.jar
   %{__ln_s} %{package_name}-servlet-%{servletspec}-api.jar %{package_name}-servlet-api.jar
   %{__mv} %{package_name}/el-api.jar %{package_name}-el-%{elspec}-api.jar
   %{__ln_s} %{package_name}-el-%{elspec}-api.jar %{package_name}-el-api.jar
popd

pushd output/build
    %{_bindir}/build-jar-repository lib jakarta-commons-collections \
                                        jakarta-commons-dbcp jakarta-commons-pool 2>&1
    # need to use -p here with b-j-r otherwise the examples webapp fails to
    # load with a java.io.IOException
    %{_bindir}/build-jar-repository -p webapps/examples/WEB-INF/lib \
    taglibs-core.jar taglibs-standard.jar 2>&1
popd

pushd ${RPM_BUILD_ROOT}%{libdir}
    # symlink JSP and servlet API jars
    %{__ln_s} ../%{package_name}-jsp-%{jspspec}-api.jar .
    %{__ln_s} ../%{package_name}-servlet-%{servletspec}-api.jar .
    %{__ln_s} ../%{package_name}-el-%{elspec}-api.jar .
    %{__ln_s} $(build-classpath jakarta-commons-collections) commons-collections.jar
    %{__ln_s} $(build-classpath jakarta-commons-dbcp) commons-dbcp.jar
    %{__ln_s} $(build-classpath jakarta-commons-pool) commons-pool.jar
    %{__ln_s} $(build-classpath log4j) log4j.jar

popd

# symlink to the FHS locations where we've installed things
pushd ${RPM_BUILD_ROOT}%{homedir}
    %{__ln_s} %{appdir} webapps
    %{__ln_s} %{confdir} conf
    %{__ln_s} %{libdir} lib
    %{__ln_s} %{logdir} logs
    %{__ln_s} %{tempdir} temp
    %{__ln_s} %{workdir} work
popd

# install sample webapp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{appdir}/sample
pushd ${RPM_BUILD_ROOT}%{appdir}/sample
%{jar} xf ${RPM_BUILD_ROOT}%{appdir}/docs/appdev/sample/sample.war
popd
%{__rm} ${RPM_BUILD_ROOT}%{appdir}/docs/appdev/sample/sample.war

# Allow linking for example webapp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{appdir}/examples/META-INF
pushd ${RPM_BUILD_ROOT}%{appdir}/examples/META-INF
echo '<?xml version="1.0" encoding="UTF-8"?>'>context.xml
echo '<Context allowLinking="true"/>'>>context.xml
popd

pushd ${RPM_BUILD_ROOT}%{appdir}/examples/WEB-INF/lib
%{__ln_s} -f $(build-classpath jakarta-taglibs-core) jstl.jar
%{__ln_s} -f $(build-classpath jakarta-taglibs-standard) standard.jar
popd


# replace temporary copy with link
%{__ln_s} -f %{bindir}/tomcat-juli.jar ${RPM_BUILD_ROOT}%{libdir}/

mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/lib/tmpfiles.d
cat > ${RPM_BUILD_ROOT}%{_prefix}/lib/tmpfiles.d/%{package_name}.conf <<EOF
f %{_localstatedir}/run/%{package_name}.pid 0644 tomcat tomcat -
EOF


%pre
# add the tomcat user and group
%{_sbindir}/groupadd -g %{tcuid} -r tomcat 2>/dev/null || :
%{_sbindir}/useradd -c "Apache Tomcat" -u %{tcuid} -g tomcat \
    -s /bin/nologin -r -d %{homedir} tomcat 2>/dev/null || :

%post
# install but don't activate
/sbin/chkconfig --add %{package_name}

%post jsp-%{jspspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/jsp.jar jsp \
    %{_javadir}/%{package_name}-jsp-%{jspspec}-api.jar 20200

%post servlet-%{servletspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/servlet.jar servlet \
    %{_javadir}/%{package_name}-servlet-%{servletspec}-api.jar 30000

%post el-%{elspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/elspec.jar elspec \
   %{_javadir}/%{package_name}-el-%{elspec}-api.jar 20300

%preun
# clean tempdir and workdir on removal or upgrade
%{__rm} -rf %{workdir}/* %{tempdir}/*
if [ "$1" = "0" ]; then
    %{_initrddir}/%{package_name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{package_name}
fi

%postun jsp-%{jspspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jsp \
        %{_javadir}/%{package_name}-jsp-%{jspspec}-api.jar
fi

%postun servlet-%{servletspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove servlet \
        %{_javadir}/%{package_name}-servlet-%{servletspec}-api.jar
fi

%postun el-%{elspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove elspec \
        %{_javadir}/%{package_name}-el-%{elspec}-api.jar
fi

%files
%defattr(0664,root,tomcat,0755)
%doc {LICENSE,NOTICE,RELEASE*}
%attr(0755,root,root) %{_bindir}/%{package_name}-digest
%attr(0755,root,root) %{_bindir}/%{package_name}-tool-wrapper
%attr(0755,root,root) %{_sbindir}/%{package_name}
%attr(0755,root,root) %{_initrddir}/%{package_name}
%attr(0755,root,root) %dir %{_libexecdir}/%{package_name}
%attr(0755,root,root) %{_libexecdir}/%{package_name}/preamble
%attr(0755,root,root) %{_libexecdir}/%{package_name}/server
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{package_name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{package_name}
%attr(0755,root,tomcat) %dir %{basedir}
%attr(0755,root,tomcat) %dir %{confdir}
%defattr(0664,tomcat,root,0770)
%attr(0770,tomcat,root) %dir %{logdir}
%defattr(0664,root,tomcat,0770)
%attr(0660,tomcat,tomcat) %{logdir}/catalina.out
%attr(0644,tomcat,tomcat) %{_localstatedir}/run/%{package_name}.pid
%attr(0770,root,tomcat) %dir %{cachedir}
%attr(0770,root,tomcat) %dir %{tempdir}
%attr(0770,root,tomcat) %dir %{workdir}
%defattr(0664,root,tomcat,0775)
%attr(0775,root,tomcat) %dir %{appdir}
%attr(0775,root,tomcat) %dir %{confdir}/Catalina
%attr(0775,root,tomcat) %dir %{confdir}/Catalina/localhost
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/%{package_name}.conf
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/*.policy
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/*.properties
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/context.xml
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/server.xml
%attr(0660,tomcat,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/web.xml
%dir %{homedir}
%{_prefix}/lib/tmpfiles.d/%{package_name}.conf
%{bindir}/bootstrap.jar
%{bindir}/catalina-tasks.xml
%{homedir}/lib
%{homedir}/temp
%{homedir}/webapps
%{homedir}/work
%{homedir}/logs
%{homedir}/conf

%files admin-webapps
%defattr(0664,root,tomcat,0755)
%{appdir}/host-manager
%{appdir}/manager

%files docs-webapp
%defattr(-,root,root,-)
%{appdir}/docs

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{package_name}

%files jsp-%{jspspec}-api
%defattr(-,root,root,-)
%{_javadir}/%{package_name}-jsp-%{jspspec}*.jar
%{_javadir}/%{package_name}-jsp-api.jar

%files lib
%defattr(-,root,root,-)
%{libdir}
%{bindir}/tomcat-juli.jar

%exclude %{libdir}/%{package_name}-el-%{elspec}-api.jar

%files servlet-%{servletspec}-api
%defattr(-,root,root,-)
%doc LICENSE
%{_javadir}/%{package_name}-servlet-%{servletspec}*.jar
%{_javadir}/%{package_name}-servlet-api.jar

%files el-%{elspec}-api
%defattr(-,root,root,-)
%doc LICENSE
%{_javadir}/%{package_name}-el-%{elspec}-api.jar
%{_javadir}/%{package_name}-el-api.jar
%{libdir}/%{package_name}-el-%{elspec}-api.jar


%files webapps
%defattr(0644,tomcat,tomcat,0755)
%{appdir}/ROOT
%{appdir}/examples
%{appdir}/sample

%changelog
* Tue Feb 25 2014 - 0:7.0.52-1
- Update to 7.0.52 upstream, fixing the following CVEs:
- CVE-2013-4322 Incomplete fix for CVE-2012-3544 (Denial of Service)
- CVE-2013-4286 Incomplete fix for CVE-2005-2090 (Information disclosure)
- CVE-2013-4590 Information disclosure via XXE when running untrusted web applications
- CVE-2014-0033 Session fixation still possible with disableURLRewriting enabled
- Replace /usr/sbin/tomcat7 wrapper with non-systemd version
- Replaced systemd init script with init.d
- Remove systemd crap
- Provide %{package_name} for compatibility
- Switched back to jakarta-commons-* names instead of apache-commons-*

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:7.0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.42-2
- Remove jpackage-utils R

* Thu Jul 11 2013 Dmitry Tikhonov <squall.sama@gmail.com> 0:7.0.42-1
- Updated to 7.0.42

* Tue Jun 11 2013 Paul Komkoff <i@stingr.net> 0:7.0.40-3
- Dropped systemv inits. Bye-bye.
- Updated the systemd wrappers to allow running multiple instances.
  Added wrapper scripts to do that, ported the original non-named
  service file to work with the same wrappers, updated
  /usr/sbin/tomcat to call systemctl.

* Sat May 11 2013 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.40-1
- Updated to 7.0.40
- Resolves: rhbz 956569 added missing commons-pool link
- Remove ant-nodeps BR

* Mon Mar  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.37-2
- Add depmaps for org.eclipse.jetty.orbit
- Resolves: rhbz#917626

* Wed Feb 20 2013 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.39-1
- Updated to 7.0.39

* Wed Feb 20 2013 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.37-1
- Updated to 7.0.37

* Mon Feb 4 2013 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.35-1
- Updated to 7.0.35
- systemd SuccessExitStatus=143 for proper stop exit code processing

* Mon Dec 24 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.34-1
- Updated to 7.0.34
- ecj >= 4.2.1 now required
- Resolves: rhbz 889395 concat classpath correctly; chdir to $CATALINA_HOME

* Fri Dec 7 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.33-2
- Resolves: rhbz 883806 refix logdir ownership 

* Sun Dec 2 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.33-1
- Updated to 7.0.33
- Resolves: rhbz 873620 need chkconfig for update-alternatives

* Wed Oct 17 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.32-1
- Updated to 7.0.32
- Resolves: rhbz 842620 symlinks to taglibs

* Fri Aug 24 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.29-1
- Updated to 7.0.29
- Add pidfile as tmpfile
- Use systemd for running as unprivileged user
- Resolves: rhbz 847751 upgrade path was broken
- Resolves: rhbz 850343 use new systemd-rpm macros

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:7.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 2 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.28-1
- Updated to 7.0.28
- Resolves: rhbz 820119 Remove bundled apache-commons-dbcp
- Resolves: rhbz 814900 Added tomcat-coyote POM
- Resolves: rhbz 810775 Remove systemv stuff from %post scriptlet
- Remove redhat-lsb R 

* Mon Apr 9 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.27-2
- Fixed native download hack

* Sat Apr 7 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.27-1
- Updated to 7.0.27
- Fixed jakarta-taglibs-standard BR and R

* Wed Mar 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:7.0.26-2
- Add more depmaps to J2EE apis to help jetty/glassfish updates

* Wed Mar 14 2012 Juan Hernandez <juan.hernandez@redhat.com> 0:7.0.26-2
- Added the POM files for tomcat-api and tomcat-util (#803495)

* Wed Feb 22 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.26-1
- Updated to 7.0.26
- Bug 790334: Change ownership of logdir for logrotate

* Thu Feb 16 2012 Krzysztof Daniel <kdaniel@redhat.com> 0:7.0.25-4
- Bug 790694: Priorities of jsp, servlet and el packages updated.

* Wed Feb 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 0:7.0.25-3
- Dropped indirect dependecy to tomcat 5

* Sun Jan 22 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.25-2
- Added hack for maven depmap of tomcat-juli absolute link [ -f ] pass correctly

* Sat Jan 21 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.25-1
- Updated to 7.0.25
- Removed EntityResolver patch (changes already in upstream sources)
- Place poms and depmaps in the same package as jars
- Added javax.servlet.descriptor to export-package of servlet-api
- Move several chkconfig actions and reqs to systemv subpackage
- New maven depmaps generation method
- Add patch to support java7. (patch sent upstream).
- Require java >= 1:1.6.0

* Fri Jan 13 2012 Krzysztof Daniel <kdaniel@redhat.com> 0:7.0.23-5
- Exported javax.servlet.* packages in version 3.0 as 2.6 to make
  servlet-api compatible with Eclipse.

* Thu Jan 12 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.23-4
- Move jsvc support to subpackage

* Wed Jan 11 2012 Alexander Kurtakov <akurtako@redhat.com> 0:7.0.23-2
- Add EntityResolver setter patch to jasper for jetty's need. (patch sent upstream).

* Mon Dec 12 2011 Joseph D. Wagner <joe@josephdwagner.info> 0:7.0.23-3
- Added support to /usr/sbin/tomcat-sysd and /usr/sbin/tomcat for
  starting tomcat with jsvc, which allows tomcat to perform some
  privileged operations (e.g. bind to a port < 1024) and then switch
  identity to a non-privileged user. Must add USE_JSVC="true" to
  /etc/tomcat/tomcat.conf or /etc/sysconfig/tomcat.

* Mon Nov 28 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.23-1
- Updated to 7.0.23

* Fri Nov 11 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.22-2
- Move tomcat-juli.jar to lib package
- Drop %%update_maven_depmap as in tomcat6
- Provide native systemd unit file ported from tomcat6

* Thu Oct 6 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.22-1
- Updated to 7.0.22

* Mon Oct 03 2011 Rex Dieter <rdieter@fedoraproject.org> - 0:7.0.21-3.1
- rebuild (java), rel-eng#4932

* Mon Sep 26 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.21-3
- Fix basedir mode

* Tue Sep 20 2011 Roland Grunberg <rgrunber@redhat.com> 0:7.0.21-2
- Add manifests for el-api, jasper-el, jasper, tomcat, and tomcat-juli.

* Thu Sep 8 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.21-1
- Updated to 7.0.21

* Mon Aug 15 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.20-3
- Require java = 1:1.6.0

* Mon Aug 15 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.20-2
- Require java < 1.7.0

* Mon Aug 15 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.20-1
- Updated to 7.0.20

* Tue Jul 26 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.19-1
- Updated to 7.0.19

* Tue Jun 21 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.16-1
- Updated to 7.0.16

* Mon Jun 6 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.14-3
- Added initial systemd service
- Fix some paths

* Sat May 21 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.14-2
- Fixed http source link
- Securify some permissions
- Added licenses for el-api and servlet-api
- Added dependency on jpackage-utils for the javadoc subpackage

* Sat May 14 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.14-1
- Updated to 7.0.14

* Thu May 5 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.12-4
- Provided local paths for libs
- Fixed dependencies
- Fixed update temp/work cleanup

* Mon May 2 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.12-3
- Fixed package groups
- Fixed some permissions
- Fixed some links
- Removed old tomcat6 crap

* Thu Apr 28 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.12-2
- Package now named just tomcat instead of tomcat7
- Removed Provides:  tomcat-log4j
- Switched to apache-commons-* names instead of jakarta-commons-* .
- Remove the old changelog
- BR/R java >= 1:1.6.0 , same for java-devel
- Removed old tomcat6 crap

* Wed Apr 27 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.12-1
- Tomcat7
