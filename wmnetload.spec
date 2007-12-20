Summary: Network monitoring dockapp for WindowMaker
Name:		wmnetload
Version:	1.3
Release:	%mkrel 2
License:	GPL
Group:		Graphical desktop/WindowMaker
Source0:	%name-%version.tar.bz2
Source10:	%name-16x16.png
Source11:	%name-32x32.png
Source12:	%name-48x48.png
URL:		ftp://truffula.com/pub/
Requires:	xpm
BuildRequires:	X11-devel, xpm-devel, dockapp-devel
Prefix:		/usr


%description
wmnetload is a network interface monitor dockapp for Window Maker. It is
designed to fit well with dockapps like wmcpuload and wmmemmon. It tracks
whether the interface is functioning and displays current network interface
throughput, along with an auto-scaling graph of recent network activity (the
graph separates upstream and downstream traffic load cleanly without
resorting to colors).

%prep

%setup -n %name-%version

%build

perl -pi -e 's/^LIBRARY_SEARCH_PATH(\s*?[^#].*$)/# \1/' configure.in
perl -pi -e 's/^LIBRARY_RPATH(\s*?[^#].*$)/# \1/' configure.in
perl -pi -e 's/^HEADER_SEARCH_PATH(\s*?[^#].*$)/# \1/' configure.in

autoconf
aclocal
automake

%configure

%make

%install
[ -d %buildroot ] && rm -rf %buildroot

%makeinstall

install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}
install -m 644 %SOURCE10 %buildroot%{_miconsdir}/%{name}.png
install -m 644 %SOURCE11 %buildroot%{_iconsdir}/%{name}.png
install -m 644 %SOURCE12 %buildroot%{_liconsdir}/%{name}.png

install -m 755 -d %buildroot%{_menudir}
cat << EOF > %buildroot%{_menudir}/%{name}
?package(%{name}):command="%{prefix}/bin/%{name}" icon="%{name}.png"\\
                 needs="wmaker" section="Applications/Monitoring" title="WmNetLoad"\\
                 longtitle="Network monitoring dockapp for WindowMaker"
EOF


%clean
[ -z %buildroot ] || {
    rm -rf %buildroot
}


%post
%{update_menus}


%postun
%{clean_menus}


%files
%defattr (-,root,root)
%doc AUTHORS INSTALL NEWS COPYING README ChangeLog
%{prefix}/bin/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_menudir}/%{name}


